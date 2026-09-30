scoreboard objectives add tb.data dummy
scoreboard objectives add tb.q dummy
scoreboard objectives add tb.mode dummy
scoreboard objectives add tb.arrows dummy
scoreboard objectives add tb.marked dummy
scoreboard objectives add tb.uid dummy
scoreboard objectives add tb.owner dummy
execute unless score #debug tb.data matches -2147483648..2147483647 run scoreboard players set #debug tb.data 0
tellraw @a {"text":"[TorchBow] loaded. 弓/クロスボウ + 松明（どちらの手でも可）で自動装填されます。","color":"gold"}
