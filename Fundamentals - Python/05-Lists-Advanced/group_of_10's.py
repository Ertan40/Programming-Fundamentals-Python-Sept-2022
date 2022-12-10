numbers = [int(item) for item in input().split(", ")]
group_boundry = 0
list_of_numbers = []
for i in range(1, 10 + 1):
    list_of_numbers.clear()
    if len(numbers) != 0:
        group_boundry += 10
        for num in numbers:
            if num <= group_boundry:
                list_of_numbers.append(num)
        for t in list_of_numbers:
            numbers.remove(t)

        print(f"Group of {group_boundry}'s: {list_of_numbers}")







# numbers = [int(item) for item in input().split(", ")]
# # [8, 12, 38, 3, 17, 19, 25, 35, 50]
# max_number = max(numbers)
#
# my_list = [num for num in numbers if 1 <= num <= 10 and num <= max_number]
# my_list_20 = [num for num in numbers if 11 <= num <= 20]
# my_list_30 = [num for num in numbers if 21 <= num <= 30]
# my_list_40 = [num for num in numbers if 31 <= num <= 40]
# my_list_50 = [num for num in numbers if 41 <= num <= 50]
# my_list_60 = [num for num in numbers if 51 <= num <= 60 and num >= max_number]
# my_list_70 = [num for num in numbers if 61 <= num <= 70 and num >= max_number]
# my_list_80 = [num for num in numbers if 71 <= num <= 80 and num <= max_number]
#
# print(f"Group of 10's: {my_list}")
# print(f"Group of 20's: {my_list_20}")
# print(f"Group of 30's: {my_list_30}")
# print(f"Group of 40's: {my_list_40}")
# print(f"Group of 50's: {my_list_50}")
# print(f"Group of 60's: {my_list_60}")
# print(f"Group of 70's: {my_list_70}")
# print(f"Group of 80's: {my_list_80}")
