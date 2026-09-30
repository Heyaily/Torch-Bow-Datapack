scoreboard players set #tb.try tb.data 0
scoreboard players set #tb.owner tb.data -1
scoreboard players operation #tb.owner tb.data = @s tb.owner
scoreboard players set #tb.hastorch tb.data 0
execute as @a if score @s tb.uid = #tb.owner tb.data run function torchbow:arrow/check_torch
execute if score #debug tb.data matches 1 run tellraw @a [{"text":"[TB] landed. shooter torches=","color":"aqua"},{"score":{"name":"#tb.hastorch","objective":"tb.data"}}]
execute if score #tb.hastorch tb.data matches 1.. run function torchbow:place/run_attempts
execute if score #tb.try tb.data matches 1 as @a[gamemode=!creative] if score @s tb.uid = #tb.owner tb.data run clear @s minecraft:torch 1
execute unless entity @s[tag=tb.marked] run function torchbow:arrow/refund_arrow
execute if score #tb.try tb.data matches 1 if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] placed torch","color":"green"}
execute unless score #tb.try tb.data matches 1 if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] nothing placed (no valid surface or no torch), nothing consumed","color":"red"}
kill @s
