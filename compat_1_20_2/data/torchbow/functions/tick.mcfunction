execute as @e[type=#torchbow:projectiles,tag=!tb.checked] run function torchbow:arrow/check
execute as @e[type=#torchbow:projectiles,tag=tb.loaded] at @s run function torchbow:arrow/poll
execute as @a unless score @s tb.uid = @s tb.uid run function torchbow:uid/assign
execute as @a[gamemode=!spectator] run function torchbow:ammo/qualify
execute as @a run function torchbow:ammo/count
execute as @a[scores={tb.q=1}] if score @s tb.arrows matches 0 run function torchbow:ammo/give
execute as @a if score @s tb.marked matches 1.. if score @s tb.arrows > @s tb.marked run function torchbow:ammo/clear
execute as @a[scores={tb.q=0}] if score @s tb.marked matches 1.. run function torchbow:ammo/clear
execute as @a run function torchbow:ammo/snapshot
