execute if entity @s[tag=tb.marked] run data modify entity @s damage set value 0.0d
execute store result score #tb.ig tb.data run data get entity @s inGround
execute if score #debug tb.data matches 1 run tellraw @a [{"text":"[TB] poll ","color":"dark_gray"},{"selector":"@s"},{"text":" inGround=","color":"dark_gray"},{"score":{"name":"#tb.ig","objective":"tb.data"}}]
execute if score #tb.ig tb.data matches 1 run function torchbow:arrow/resolve
