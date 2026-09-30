execute store success score #tb.set tb.data run setblock ~ ~ ~ minecraft:wall_torch[facing=east]
execute if score #tb.set tb.data matches 1 run scoreboard players set #tb.try tb.data 1
execute if score #tb.set tb.data matches 1 if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] placed wall torch (east)","color":"green"}
execute if score #tb.set tb.data matches 1 run function torchbow:place/fx
