numbers = input().split()
count_of_numbers_to_remove = int(input())
final_list = []
str_final_list = []
for current_number in numbers:
    final_list.append(int(current_number))
for number in range(count_of_numbers_to_remove):
    min_number = min(final_list)
    final_list.remove(min_number)
for number in range(len(final_list)):
    final_list[number] = str(final_list[number])
print(", ".join(final_list))


