scoreboard players set @s tb.q 0
execute if entity @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:torch"}],SelectedItem:{id:"minecraft:bow"}}] run scoreboard players set @s tb.q 1
execute if entity @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:torch"}],SelectedItem:{id:"minecraft:crossbow"}}] run scoreboard players set @s tb.q 1
execute if entity @s[nbt={SelectedItem:{id:"minecraft:torch"},Inventory:[{Slot:-106b,id:"minecraft:bow"}]}] run scoreboard players set @s tb.q 1
execute if entity @s[nbt={SelectedItem:{id:"minecraft:torch"},Inventory:[{Slot:-106b,id:"minecraft:crossbow"}]}] run scoreboard players set @s tb.q 1
