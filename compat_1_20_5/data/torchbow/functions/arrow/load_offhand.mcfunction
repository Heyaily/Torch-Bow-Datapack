tag @e[tag=tb.current,limit=1] add tb.loaded
scoreboard players operation @e[tag=tb.current,limit=1] tb.owner = @s tb.uid
execute if score @s tb.mode matches 1 run data modify entity @e[tag=tb.current,limit=1] damage set value 0.0d
execute if score @s tb.mode matches 1 run tag @e[tag=tb.current,limit=1] add tb.marked
execute if score @s tb.mode matches 1 if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] dummy ammo fired","color":"aqua"}
execute if score @s tb.mode matches 0 if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] real arrow used","color":"aqua"}
playsound minecraft:block.lantern.place player @s ~ ~ ~ 0.5 1.6
execute if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] tb.loaded tag applied","color":"green"}
