tag @s add tb.checked
tag @s add tb.current
execute on owner run function torchbow:arrow/check_owner
execute if score #debug tb.data matches 1 unless entity @s[tag=tb.loaded] run tellraw @a {"text":"[TB] owner path did not tag this arrow, trying nearest-player fallback","color":"aqua"}
execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] if items entity @s weapon.offhand minecraft:torch if items entity @s weapon.mainhand #torchbow:launchers run function torchbow:arrow/load_offhand
execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] if items entity @s weapon.mainhand minecraft:torch if items entity @s weapon.offhand #torchbow:launchers run function torchbow:arrow/load_mainhand
execute if score #debug tb.data matches 1 unless entity @s[tag=tb.loaded] run tellraw @a {"text":"[TB] fallback also failed to find a qualifying nearby player","color":"red"}
tag @s remove tb.current
