quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
ornament_sets_price = 2
skirts_price = 5
garland_price = 3
lights_price = 15
day_counter = 0
spent_money = 0
total_spirit = 0
for current_day in range(days_left_until_christmas):
    day_counter += 1
    if day_counter % 11 == 0:
        quantity_of_decorations += 2
    if day_counter % 2 == 0:
        spent_money += (ornament_sets_price * quantity_of_decorations)
        total_spirit += 5
    if day_counter % 3 == 0:
        spent_money += (skirts_price * quantity_of_decorations) + (garland_price * quantity_of_decorations)
        total_spirit += 13
    if day_counter % 5 == 0:
        spent_money += (lights_price * quantity_of_decorations)
        total_spirit += 17
        if day_counter % 3 == 0:
            total_spirit += 30
    if day_counter % 10 == 0:
        total_spirit -= 20
        spent_money += lights_price + skirts_price + garland_price
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {spent_money}")
print(f"Total spirit: {total_spirit}")
