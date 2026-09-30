scoreboard players set @s tb.q 0
execute if items entity @s weapon.offhand minecraft:torch if items entity @s weapon.mainhand #torchbow:launchers run scoreboard players set @s tb.q 1
execute if items entity @s weapon.mainhand minecraft:torch if items entity @s weapon.offhand #torchbow:launchers run scoreboard players set @s tb.q 1
