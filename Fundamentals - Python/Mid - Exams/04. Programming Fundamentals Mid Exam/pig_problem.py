quantity_of_food_in_gr = float(input()) * 1000
quantity_hay_in_gr = float(input()) * 1000
quantity_cover_in_gr = float(input()) * 1000
weight_in_gr = float(input()) * 1000
for current_day in range(1, 30 + 1):
    quantity_of_food_in_gr -= 300
    if current_day % 2 == 0:
        quantity_hay_in_gr -= quantity_of_food_in_gr * 0.05
    if current_day % 3 == 0:
        quantity_cover_in_gr -= weight_in_gr / 3
    if quantity_of_food_in_gr <= 0 or quantity_hay_in_gr <= 0 or quantity_cover_in_gr <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food_in_gr / 1000:.2f},\
    Hay: {quantity_hay_in_gr / 1000:.2f}, Cover: {quantity_cover_in_gr / 1000:.2f}.")

# quantity_food_in_kilograms = float(input())
# quantity_hay_in_kilograms = float(input())
# quantity_cover_in_kilograms = float(input())
# weight_in_kilograms = float(input())
# quantity_food_in_grams = quantity_food_in_kilograms * 1000
# quantity_hay_in_grams = quantity_hay_in_kilograms * 1000
# quantity_cover_in_grams = quantity_cover_in_kilograms * 1000
# weight_in_grams = weight_in_kilograms * 1000
# is_food_not_left = False
# month_days = 30
# for day in range(1, month_days + 1):
#     quantity_food_in_grams -= 300
#     if quantity_food_in_grams <= 0:
#         is_food_not_left = True
#
#     if day % 2 == 0:
#         quantity_hay_in_grams -= quantity_food_in_grams * (5 / 100)
#         if quantity_hay_in_grams <= 0:
#             is_food_not_left = True
#
#     if day % 3 == 0:
#         quantity_cover_in_grams -= weight_in_grams * 1 / 3
#         if quantity_cover_in_grams <= 0:
#             is_food_not_left = True
#
#     if is_food_not_left:
#         print('Merry must go to the pet store!')
#         break
#
# if not is_food_not_left:
#     print('Everything is fine! Puppy is happy! ' \
#           f'Food: {quantity_food_in_grams / 1000:.2f}, ' \
#           f'Hay: {quantity_hay_in_grams / 1000:.2f}, ' \
#           f'Cover: {quantity_cover_in_grams / 1000:.2f}.')
