#!/usr/bin/env python3
"""Generate the compat overlays and all release zips for TorchBow."""
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
DESC = "TorchBow - place torches by shooting arrows"
DIR_MAP = {"function": "functions", "block": "blocks", "item": "items", "entity_type": "entity_types"}
LAUNCHERS = ["bow", "crossbow"]

# Per-language "this zip is for version X (format N)" banner, inserted right
# after each "### 対応バージョン"-equivalent heading. {v} = version label,
# {f} = pack format number(s).
VERSION_BANNER = {
    "### 対応バージョン\n": "### 対応バージョン\nこの zip は **Minecraft Java Edition {v}**（データパックフォーマット {f}）向けです。他のバージョンをお使いの場合は、Releases ページで別のファイルを探してください。\n",
    "### Supported versions\n": "### Supported versions\nThis zip is for **Minecraft Java Edition {v}** (data pack format {f}). If you are on a different version, look for the matching file on the Releases page.\n",
    "### 支持的版本\n": "### 支持的版本\n此 zip 适用于 **Minecraft Java Edition {v}**（数据包格式 {f}）。如果你使用的是其他版本，请在 Releases 页面查找对应的文件。\n",
    "### Versions prises en charge\n": "### Versions prises en charge\nCe zip est destiné à **Minecraft Java Edition {v}** (format de data pack {f}). Si vous utilisez une autre version, cherchez le fichier correspondant sur la page Releases.\n",
    "### Versiones compatibles\n": "### Versiones compatibles\nEste zip es para **Minecraft Java Edition {v}** (formato de data pack {f}). Si usas otra versión, busca el archivo correspondiente en la página de Releases.\n",
    "### 지원 버전\n": "### 지원 버전\n이 zip은 **Minecraft Java Edition {v}** (데이터 팩 형식 {f}) 전용입니다. 다른 버전을 사용 중이라면 Releases 페이지에서 해당 파일을 찾아주세요.\n",
}


def readme_for(version_label, format_desc):
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for heading, banner in VERSION_BANNER.items():
        assert heading in text, heading
        text = text.replace(heading, banner.format(v=version_label, f=format_desc), 1)
    return text

# (pack_format, file suffix) for versions that cannot use overlays
LEGACY_BUILDS = [
    (4, "1.13-1.14.4"), (5, "1.15-1.16.1"), (6, "1.16.2-1.16.5"), (7, "1.17-1.17.1"),
    (8, "1.18-1.18.1"), (9, "1.18.2"), (10, "1.19-1.19.3"), (12, "1.19.4"), (15, "1.20-1.20.1"),
]
# entity_type tags (the "#namespace:tag" part of a "type=" selector) were only
# added in a 1.14 snapshot, so format 4 (which also covers 1.13) cannot use them.
NO_ENTITY_TAG_FORMATS = {4}
# (directory, min format, max format, uses legacy NBT syntax)
OVERLAYS = [("compat_1_20_5", 41, 47, False), ("compat_1_20_2", 18, 40, True)]

FORBIDDEN_LEGACY = [r"if items", r"unless items", r"on owner", r"\breturn\b", r"custom_data", r"count:1", r"weapon\."]


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def nbt_cfg(torch_hand, launcher):
    def part(hand, item):
        if hand == "off":
            return 'Inventory:[{Slot:-106b,id:"minecraft:%s"}]' % item
        return 'SelectedItem:{id:"minecraft:%s"}' % item
    launcher_hand = "main" if torch_hand == "off" else "off"
    return "nbt={%s,%s}" % (part(torch_hand, "torch"), part(launcher_hand, launcher))


def legacy_files(no_entity_tag=False):
    files = {}
    if no_entity_tag:
        types = json.loads((ROOT / "data/torchbow/tags/entity_type/projectiles.json").read_text(encoding="utf-8"))["values"]
        src = (ROOT / "data/torchbow/function/tick.mcfunction").read_text(encoding="utf-8")
        # entity_type tags don't exist yet: expand "type=#torchbow:projectiles"
        # into one explicit line per concrete type it lists.
        lines = []
        for line in src.splitlines():
            if "type=#torchbow:projectiles" in line:
                lines.extend(line.replace("type=#torchbow:projectiles", "type=%s" % t) for t in types)
            else:
                lines.append(line)
        files["torchbow/function/tick.mcfunction"] = "\n".join(lines) + "\n"
    q = ["scoreboard players set @s tb.q 0"]
    for th in ("off", "main"):
        for l in LAUNCHERS:
            q.append("execute if entity @s[%s] run scoreboard players set @s tb.q 1" % nbt_cfg(th, l))
    files["torchbow/function/ammo/qualify.mcfunction"] = "\n".join(q) + "\n"

    c = ["tag @s add tb.checked", "tag @s add tb.current"]
    for th, fn in (("off", "load_offhand"), ("main", "load_mainhand")):
        for l in LAUNCHERS:
            c.append(
                "execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] "
                "if entity @s[%s] run function torchbow:arrow/%s" % (nbt_cfg(th, l), fn))
    c.append('execute if score #debug tb.data matches 1 unless entity @s[tag=tb.loaded] run tellraw @a {"text":"[TB] no qualifying nearby player found","color":"red"}')
    c.append("tag @s remove tb.current")
    files["torchbow/function/arrow/check.mcfunction"] = "\n".join(c) + "\n"

    files["torchbow/function/ammo/give.mcfunction"] = (
        "give @s minecraft:arrow{torchbow:1b}\nscoreboard players set @s tb.marked 1\nscoreboard players set @s tb.arrows 1\n")
    files["torchbow/function/ammo/clear.mcfunction"] = (
        "clear @s minecraft:arrow{torchbow:1b}\nscoreboard players set @s tb.marked 0\n")
    files["torchbow/function/ammo/count.mcfunction"] = (
        "execute store result score @s tb.arrows run clear @s #minecraft:arrows 0\n"
        "execute store result score @s tb.marked run clear @s minecraft:arrow{torchbow:1b} 0\n")

    src = (ROOT / "data/torchbow/function/arrow/refund_arrow.mcfunction").read_text(encoding="utf-8")
    files["torchbow/function/arrow/refund_arrow.mcfunction"] = src.replace("count:1", "Count:1b")

    t = ['execute if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] try: checking candidate position","color":"gray"}']
    checks = [("~ ~-1 ~", "set_floor"), ("~ ~ ~-1", "set_wall_south"), ("~ ~ ~1", "set_wall_north"),
              ("~1 ~ ~", "set_wall_west"), ("~-1 ~ ~", "set_wall_east")]
    for pos, fn in checks:
        t.append("execute if block ~ ~ ~ #torchbow:replaceable unless score #tb.try tb.data matches 1 "
                 "unless block %s #torchbow:no_support run function torchbow:place/%s" % (pos, fn))
    files["torchbow/function/place/try.mcfunction"] = "\n".join(t) + "\n"
    return files


LEGACY_SKIP = {"torchbow/function/arrow/check_owner.mcfunction", "torchbow/tags/item/launchers.json"}


def plural_rel(rel):
    parts = list(rel.parts)
    if len(parts) >= 2 and parts[1] == "function":
        parts[1] = "functions"
    elif len(parts) >= 3 and parts[1] == "tags" and parts[2] in DIR_MAP:
        parts[2] = DIR_MAP[parts[2]]
    return Path(*parts)


def build_tree(dst_data, plural, legacy, no_entity_tag=False):
    dst_data = Path(dst_data)
    if dst_data.exists():
        shutil.rmtree(dst_data)
    lfiles = legacy_files(no_entity_tag) if legacy else {}
    for src in sorted((ROOT / "data").rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(ROOT / "data")
        key = rel.as_posix()
        out = dst_data / (plural_rel(rel) if plural else rel)
        if legacy:
            if key in LEGACY_SKIP:
                continue
            if no_entity_tag and key == "torchbow/tags/entity_type/projectiles.json":
                continue
            if key in lfiles:
                write(out, lfiles[key])
                continue
            if key == "torchbow/tags/block/replaceable.json":
                data = json.loads(src.read_text(encoding="utf-8"))
                data["values"].append({"id": "minecraft:grass", "required": False})
                write(out, json.dumps(data, indent=2) + "\n")
                continue
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, out)


def validate_tree(data_dir, plural, legacy, label, no_entity_tag=False):
    data_dir = Path(data_dir)
    fdir = "functions" if plural else "function"
    tag_dirs = [DIR_MAP[k] if plural else k for k in DIR_MAP if k != "function"]
    problems = []
    for f in data_dir.rglob("*.mcfunction"):
        text = f.read_text(encoding="utf-8")
        if "  " in text:
            problems.append("%s: double space in %s" % (label, f))
        if re.search(r"^\s*#", text, re.M):
            problems.append("%s: comment left in %s" % (label, f))
        if legacy:
            for pat in FORBIDDEN_LEGACY:
                if re.search(pat, text):
                    problems.append("%s: forbidden %r in %s" % (label, pat, f))
        if no_entity_tag and "type=#" in text:
            problems.append("%s: entity_type tag used in %s (unsupported before 1.14)" % (label, f))
        for ns, path in re.findall(r"function (\w+):([\w/]+)", text):
            if not (data_dir / ns / fdir / (path + ".mcfunction")).exists():
                problems.append("%s: missing function %s:%s (from %s)" % (label, ns, path, f.name))
        for ns, path in re.findall(r"#(torchbow):([\w/]+)", text):
            if not any((data_dir / ns / "tags" / d / (path + ".json")).exists() for d in tag_dirs):
                problems.append("%s: missing tag #%s:%s (from %s)" % (label, ns, path, f.name))
    for j in data_dir.rglob("*.json"):
        try:
            json.loads(j.read_text(encoding="utf-8"))
        except Exception as e:
            problems.append("%s: bad json %s (%s)" % (label, j, e))
    if not list(data_dir.rglob("*.mcfunction")):
        problems.append("%s: no functions" % label)
    return problems


def make_zip(zip_path, entries):
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for arcname, path in entries:
            z.write(path, arcname)


def tree_entries(base, prefix=""):
    base = Path(base)
    return [((prefix + p.relative_to(base).as_posix()), p) for p in sorted(base.rglob("*")) if p.is_file()]


def main():
    problems = []
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    entries_meta = []
    for d, lo, hi, legacy in OVERLAYS:
        base = ROOT / d
        if base.exists():
            shutil.rmtree(base)
        build_tree(base / "data", plural=True, legacy=legacy)
        problems += validate_tree(base / "data", True, legacy, d)
        entries_meta.append({"directory": d, "formats": [lo, hi], "min_format": lo, "max_format": hi})
    problems += validate_tree(ROOT / "data", False, False, "base")

    main_meta = {
        "pack": {"description": DESC, "pack_format": 48, "supported_formats": [18, 81], "min_format": 18, "max_format": 121},
        "overlays": {"entries": entries_meta},
    }
    write(ROOT / "pack.mcmeta", json.dumps(main_meta, indent=2) + "\n")

    tmp = DIST / "_tmp"
    main_readme = tmp / "README-main.md"
    write(main_readme, readme_for("1.20.2 \u2013 26.3", "18 \u2013 121"))
    entries = [("pack.mcmeta", ROOT / "pack.mcmeta"), ("README.md", main_readme)]
    entries += tree_entries(ROOT / "data", "data/")
    for d, *_ in OVERLAYS:
        entries += tree_entries(ROOT / d, d + "/")
    make_zip(DIST / "TorchBow.zip", entries)

    for fmt, label in LEGACY_BUILDS:
        no_et = fmt in NO_ENTITY_TAG_FORMATS
        t = tmp / str(fmt)
        build_tree(t / "data", plural=True, legacy=True, no_entity_tag=no_et)
        problems += validate_tree(t / "data", True, True, "format %d" % fmt, no_entity_tag=no_et)
        write(t / "pack.mcmeta", json.dumps({"pack": {"pack_format": fmt, "description": DESC}}, indent=2) + "\n")
        readme_path = t / "README.md"
        write(readme_path, readme_for(label.replace("-", " \u2013 "), str(fmt)))
        e = [("pack.mcmeta", t / "pack.mcmeta"), ("README.md", readme_path)] + tree_entries(t / "data", "data/")
        make_zip(DIST / ("TorchBow-%s.zip" % label), e)
    shutil.rmtree(tmp)

    if problems:
        print("PROBLEMS:")
        print("\n".join(problems))
        sys.exit(1)
    print("build ok:", ", ".join(sorted(p.name for p in DIST.iterdir())))


if __name__ == "__main__":
    main()
