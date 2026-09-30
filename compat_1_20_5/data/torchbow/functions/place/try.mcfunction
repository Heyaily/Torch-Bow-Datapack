execute if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] try: checking candidate position","color":"gray"}
execute unless block ~ ~ ~ #torchbow:replaceable run return 0
execute unless block ~ ~-1 ~ #torchbow:no_support run function torchbow:place/set_floor
execute if score #tb.try tb.data matches 1 run return 1
execute unless block ~ ~ ~-1 #torchbow:no_support run function torchbow:place/set_wall_south
execute if score #tb.try tb.data matches 1 run return 1
execute unless block ~ ~ ~1 #torchbow:no_support run function torchbow:place/set_wall_north
execute if score #tb.try tb.data matches 1 run return 1
execute unless block ~1 ~ ~ #torchbow:no_support run function torchbow:place/set_wall_west
execute if score #tb.try tb.data matches 1 run return 1
execute unless block ~-1 ~ ~ #torchbow:no_support run function torchbow:place/set_wall_east
execute if score #tb.try tb.data matches 1 run return 1
return 0
