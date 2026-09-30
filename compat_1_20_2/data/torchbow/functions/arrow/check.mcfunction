tag @s add tb.checked
tag @s add tb.current
execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] if entity @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:torch"}],SelectedItem:{id:"minecraft:bow"}}] run function torchbow:arrow/load_offhand
execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] if entity @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:torch"}],SelectedItem:{id:"minecraft:crossbow"}}] run function torchbow:arrow/load_offhand
execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] if entity @s[nbt={SelectedItem:{id:"minecraft:torch"},Inventory:[{Slot:-106b,id:"minecraft:bow"}]}] run function torchbow:arrow/load_mainhand
execute unless entity @s[tag=tb.loaded] at @s as @a[distance=..2,gamemode=!spectator,limit=1,sort=nearest] if entity @s[nbt={SelectedItem:{id:"minecraft:torch"},Inventory:[{Slot:-106b,id:"minecraft:crossbow"}]}] run function torchbow:arrow/load_mainhand
execute if score #debug tb.data matches 1 unless entity @s[tag=tb.loaded] run tellraw @a {"text":"[TB] no qualifying nearby player found","color":"red"}
tag @s remove tb.current
