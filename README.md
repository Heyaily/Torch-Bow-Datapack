# TorchBow

Minecraft Java Edition 26.2 (data pack format 107.1)

[日本語](#日本語) | [English](#english) | [中文](#中文) | [Français](#français) | [Español](#español) | [한국어](#한국어)

## Supported versions / 対応バージョン

| Minecraft Java Edition | Pack format | File |
|---|---|---|
| 1.20.2 – 26.3 | 18 – 121 | `TorchBow.zip` |
| 1.20 – 1.20.1 | 15 | `TorchBow-1.20-1.20.1.zip` |
| 1.19.4 | 12 | `TorchBow-1.19.4.zip` |
| 1.19 – 1.19.3 | 10 | `TorchBow-1.19-1.19.3.zip` |
| 1.18.2 | 9 | `TorchBow-1.18.2.zip` |
| 1.18 – 1.18.1 | 8 | `TorchBow-1.18-1.18.1.zip` |
| 1.17 – 1.17.1 | 7 | `TorchBow-1.17-1.17.1.zip` |
| 1.16.2 – 1.16.5 | 6 | `TorchBow-1.16.2-1.16.5.zip` |
| 1.15 – 1.16.1 | 5 | `TorchBow-1.15-1.16.1.zip` |
| 1.13 – 1.14.4 | 4 | `TorchBow-1.13-1.14.4.zip` |

Not supported / 非対応: pack format 1-3 (1.6.1-1.12.2, data packs did not exist yet), pack format 122 and later (26.4+, not yet confirmed).

---

## 日本語

弓やクロスボウで矢を撃つと、着弾した地面や壁にたいまつを設置できるデータパックです。

### 使い方
1. 片方の手に「たいまつ」、もう片方の手に「弓」または「クロスボウ」を持ちます（どちらの手でも可）。
2. 矢を1本も持っていない場合は、専用の矢が自動で1本渡されます。
3. 撃つと、矢が刺さった地面や壁にたいまつが設置されます。

### 仕様
- たいまつは、設置できたときだけ1個消費されます（クリエイティブでは消費されません）。
- 設置できなかったとき（水中・溶岩・支えがない・天井など）は、何も消費されません。
- 元から持っていた矢で設置したときは、矢がインベントリに返却されます。
- 専用の矢は、矢を1本も持っていないときだけ渡され、装備を外すと回収されます。
- 矢がモブに当たった場合は設置されず、たいまつも消費されません。
- 専用の矢のダメージは0になるよう設定していますが、完全に0になることは保証できません。

### 対応バージョン
上の表から、お使いのMinecraftのバージョンに合うzipを選んでください。動作確認は 26.2 のみで、それ以外のバージョンは未確認です（不具合があれば Issues で報告してください）。

### 導入
1. このリポジトリの「Releases」ページから、お使いのバージョンのzip（上の表を参照）をダウンロードし、ワールドの `datapacks` フォルダに入れます（緑の「Code」ボタンの「Download ZIP」は、フォルダ構造が異なり読み込めないため使わないでください）。
2. ゲーム内で `/reload` を実行します。

### デバッグ
`/scoreboard players set #debug tb.data 1` で動作ログが表示されます。`0` に戻すと非表示になります。

---

## English

A data pack that lets you place torches by shooting arrows from a bow or crossbow. The torch is placed on the ground or wall where the arrow lands.

### How to use
1. Hold a torch in one hand and a bow or crossbow in the other (either hand works).
2. If you have no arrows at all, a special arrow is given to you automatically.
3. Shoot. A torch is placed where the arrow sticks into the ground or a wall.

### Behavior
- A torch is consumed only when one is actually placed (not consumed in Creative mode).
- If nothing can be placed (water, lava, no support, ceiling, etc.), nothing is consumed.
- If you placed a torch using your own arrow, the arrow is returned to your inventory.
- The special arrow is only given when you have no arrows, and is removed when you stop holding the gear.
- If the arrow hits a mob, no torch is placed and no torch is consumed.
- The special arrow is set to deal 0 damage, but this cannot be fully guaranteed.

### Supported versions
Choose the zip that matches your Minecraft version from the table above. Only 26.2 has been verified; other versions are untested (please report problems via Issues).

### Installation
1. Download the zip for your version (see the table above) from the Releases page of this repository and put it into your world's `datapacks` folder (do not use the green Code → Download ZIP button; its folder structure will not load).
2. Run `/reload` in game.

### Debugging
Run `/scoreboard players set #debug tb.data 1` to show logs. Set it back to `0` to hide them.

---

## 中文

这是一个数据包：用弓或弩射出箭矢后，可以在箭矢落点的地面或墙壁上放置火把。

### 使用方法
1. 一只手拿火把，另一只手拿弓或弩（左右手均可）。
2. 如果你身上没有任何箭矢，会自动获得一支专用箭矢。
3. 射击后，火把会被放置在箭矢插入的地面或墙壁上。

### 规则
- 只有在成功放置火把时才会消耗一个火把（创造模式下不消耗）。
- 无法放置时（水中、岩浆、没有支撑、天花板等）不会消耗任何物品。
- 如果使用自己原有的箭矢成功放置火把，箭矢会返还到你的背包。
- 专用箭矢只会在你没有任何箭矢时提供，取下装备后会被收回。
- 箭矢击中生物时不会放置火把，也不会消耗火把。
- 专用箭矢被设置为造成 0 点伤害，但无法保证一定为 0。

### 支持的版本
请根据上表选择与你的 Minecraft 版本对应的 zip。目前仅在 26.2 上验证过，其他版本尚未测试（如有问题请通过 Issues 反馈）。

### 安装
1. 从本仓库的 Releases 页面下载对应版本的 zip（见上表），放入世界的 `datapacks` 文件夹（请不要使用绿色 Code 按钮中的 Download ZIP，其目录结构无法被加载）。
2. 在游戏中执行 `/reload`。

### 调试
执行 `/scoreboard players set #debug tb.data 1` 可显示运行日志，改回 `0` 即可关闭。

---

## Français

Un data pack qui permet de poser des torches en tirant des flèches avec un arc ou une arbalète. La torche est posée sur le sol ou le mur là où la flèche se plante.

### Utilisation
1. Tenez une torche dans une main et un arc ou une arbalète dans l'autre (n'importe quelle main).
2. Si vous n'avez aucune flèche, une flèche spéciale vous est donnée automatiquement.
3. Tirez. Une torche est posée là où la flèche se plante dans le sol ou un mur.

### Fonctionnement
- Une torche n'est consommée que lorsqu'elle est réellement posée (pas en mode Créatif).
- Si rien ne peut être posé (eau, lave, aucun support, plafond, etc.), rien n'est consommé.
- Si vous posez une torche avec votre propre flèche, la flèche est rendue dans votre inventaire.
- La flèche spéciale n'est donnée que si vous n'avez aucune flèche, et elle est retirée quand vous ne tenez plus l'équipement.
- Si la flèche touche un monstre, aucune torche n'est posée ni consommée.
- La flèche spéciale est réglée pour infliger 0 dégât, mais cela ne peut pas être garanti à 100 %.

### Versions prises en charge
Choisissez dans le tableau ci-dessus le zip correspondant à votre version de Minecraft. Seule la version 26.2 a été vérifiée ; les autres versions ne sont pas testées (signalez les problèmes via Issues).

### Installation
1. Téléchargez le zip de votre version (voir le tableau ci-dessus) depuis la page Releases de ce dépôt et placez-le dans le dossier `datapacks` de votre monde (n'utilisez pas le bouton vert Code → Download ZIP : sa structure ne sera pas chargée).
2. Exécutez `/reload` en jeu.

### Débogage
Exécutez `/scoreboard players set #debug tb.data 1` pour afficher les journaux. Remettez `0` pour les masquer.

---

## Español

Un data pack que permite colocar antorchas disparando flechas con un arco o una ballesta. La antorcha se coloca en el suelo o la pared donde se clava la flecha.

### Cómo usarlo
1. Sostén una antorcha en una mano y un arco o una ballesta en la otra (cualquier mano).
2. Si no tienes ninguna flecha, se te da automáticamente una flecha especial.
3. Dispara. Se coloca una antorcha donde la flecha se clava en el suelo o en una pared.

### Comportamiento
- Solo se consume una antorcha cuando realmente se coloca (no se consume en modo Creativo).
- Si no se puede colocar nada (agua, lava, sin soporte, techo, etc.), no se consume nada.
- Si colocas una antorcha con tu propia flecha, la flecha se devuelve a tu inventario.
- La flecha especial solo se entrega cuando no tienes flechas y se retira al dejar de sostener el equipo.
- Si la flecha golpea a una criatura, no se coloca ninguna antorcha ni se consume.
- La flecha especial está configurada para hacer 0 de daño, pero no se puede garantizar por completo.

### Versiones compatibles
Elige en la tabla anterior el zip que corresponda a tu versión de Minecraft. Solo se ha verificado la 26.2; las demás versiones no están probadas (informa de los problemas en Issues).

### Instalación
1. Descarga el zip de tu versión (ver la tabla anterior) desde la página de Releases de este repositorio y colócalo en la carpeta `datapacks` de tu mundo (no uses el botón verde Code → Download ZIP: su estructura no se cargará).
2. Ejecuta `/reload` en el juego.

### Depuración
Ejecuta `/scoreboard players set #debug tb.data 1` para mostrar los registros. Vuelve a poner `0` para ocultarlos.

---

## 한국어

활이나 쇠뇌로 화살을 쏘면, 화살이 꽂힌 바닥이나 벽에 횃불을 설치할 수 있는 데이터 팩입니다.

### 사용 방법
1. 한 손에 횃불, 다른 손에 활 또는 쇠뇌를 듭니다 (어느 손이든 상관없습니다).
2. 화살이 하나도 없으면 전용 화살이 자동으로 지급됩니다.
3. 발사하면 화살이 꽂힌 바닥이나 벽에 횃불이 설치됩니다.

### 동작
- 횃불은 실제로 설치되었을 때만 1개 소모됩니다 (크리에이티브 모드에서는 소모되지 않음).
- 설치할 수 없는 경우(물, 용암, 지지대 없음, 천장 등)에는 아무것도 소모되지 않습니다.
- 원래 가지고 있던 화살로 설치한 경우, 화살이 인벤토리로 반환됩니다.
- 전용 화살은 화살이 하나도 없을 때만 지급되며, 장비를 내려놓으면 회수됩니다.
- 화살이 몹에 맞으면 횃불이 설치되지 않고 소모되지도 않습니다.
- 전용 화살의 피해는 0으로 설정되어 있지만, 완전히 0이 된다고 보장할 수는 없습니다.

### 지원 버전
위 표에서 사용 중인 Minecraft 버전에 맞는 zip을 선택하세요. 26.2 에서만 동작을 확인했으며 다른 버전은 테스트되지 않았습니다 (문제가 있으면 Issues 로 알려 주세요).

### 설치
1. 이 저장소의 Releases 페이지에서 버전에 맞는 zip (위 표 참고)을 다운로드하여 월드의 `datapacks` 폴더에 넣습니다 (초록색 Code 버튼의 Download ZIP 은 구조가 달라 로드되지 않으므로 사용하지 마세요).
2. 게임에서 `/reload` 를 실행합니다.

### 디버그
`/scoreboard players set #debug tb.data 1` 을 실행하면 로그가 표시됩니다. `0` 으로 되돌리면 숨겨집니다.
