scoreboard players set #tb.owner tb.data -1
scoreboard players operation #tb.owner tb.data = @s tb.owner
scoreboard players set #tb.given tb.data 0
execute as @a if score @s tb.uid = #tb.owner tb.data run scoreboard players set #tb.given tb.data 1
execute as @a if score @s tb.uid = #tb.owner tb.data run give @s minecraft:arrow
execute if score #tb.given tb.data matches 0 run summon minecraft:item ~ ~ ~ {Item:{id:"minecraft:arrow",count:1},PickupDelay:0s}
execute if score #debug tb.data matches 1 if score #tb.given tb.data matches 1 run tellraw @a {"text":"[TB] arrow returned to the shooter","color":"aqua"}
execute if score #debug tb.data matches 1 if score #tb.given tb.data matches 0 run tellraw @a {"text":"[TB] shooter not found - arrow dropped","color":"yellow"}
