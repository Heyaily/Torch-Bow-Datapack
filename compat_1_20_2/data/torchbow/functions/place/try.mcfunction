execute if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] try: checking candidate position","color":"gray"}
execute if block ~ ~ ~ #torchbow:replaceable unless score #tb.try tb.data matches 1 unless block ~ ~-1 ~ #torchbow:no_support run function torchbow:place/set_floor
execute if block ~ ~ ~ #torchbow:replaceable unless score #tb.try tb.data matches 1 unless block ~ ~ ~-1 #torchbow:no_support run function torchbow:place/set_wall_south
execute if block ~ ~ ~ #torchbow:replaceable unless score #tb.try tb.data matches 1 unless block ~ ~ ~1 #torchbow:no_support run function torchbow:place/set_wall_north
execute if block ~ ~ ~ #torchbow:replaceable unless score #tb.try tb.data matches 1 unless block ~1 ~ ~ #torchbow:no_support run function torchbow:place/set_wall_west
execute if block ~ ~ ~ #torchbow:replaceable unless score #tb.try tb.data matches 1 unless block ~-1 ~ ~ #torchbow:no_support run function torchbow:place/set_wall_east
