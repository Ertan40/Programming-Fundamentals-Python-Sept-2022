budget = float(input())
price_for_1kg_flour = float(input())
one_pack_egg = price_for_1kg_flour * 0.75
price_for_1l_milk = price_for_1kg_flour * 1.25
total_price_for_loave = one_pack_egg + (price_for_1l_milk * 0.25) + price_for_1kg_flour
loaves_counter = 0
colored_eggs_counter = 0

while budget >= total_price_for_loave:
        loaves_counter += 1
        colored_eggs_counter += 3
        budget -= total_price_for_loave
        if loaves_counter % 3 == 0:
            colored_eggs_counter -= (loaves_counter - 2)

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")