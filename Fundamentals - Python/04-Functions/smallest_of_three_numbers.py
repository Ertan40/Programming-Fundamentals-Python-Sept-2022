def find_smallest(some_numbers):
    return min(some_numbers)

number_one = int(input())
number_two = int(input())
number_three = int(input())
my_list = [number_one, number_two, number_three]
min_number = find_smallest(my_list)
print(min_number)
