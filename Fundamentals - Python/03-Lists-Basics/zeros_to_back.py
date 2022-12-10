numbers = input().split(", ")
my_list = []
for num in numbers:
    my_list.append(int(num))
non_zero_values = [i for i in my_list if i != 0]
zeros = [j for j in my_list if j == 0]

my_list = non_zero_values + zeros
print(my_list)