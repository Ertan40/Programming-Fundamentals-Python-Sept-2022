factor_number = int(input())
count_number = int(input())
my_list = []
for current_number in range(1, count_number +1):
    current_number *= factor_number
    my_list.append(current_number)
print(my_list)