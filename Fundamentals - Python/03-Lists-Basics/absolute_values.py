numbers = input().split()
final_list = []
numbers_as_digits = [float(item) for item in numbers]
for num in numbers_as_digits:
    final_list.append(abs(num))
print(final_list)