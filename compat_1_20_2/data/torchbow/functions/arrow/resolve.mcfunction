execute if score #debug tb.data matches 1 run tellraw @a {"text":"[TB] resolve() invoked","color":"dark_aqua"}
tag @s remove tb.loaded
function torchbow:arrow/attempt_place
