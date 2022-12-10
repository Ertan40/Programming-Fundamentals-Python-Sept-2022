numbers = input().split()
rounded_numbers = []
numbers_as_digits = [float(item) for item in numbers]
for num in numbers_as_digits:
    rounded_numbers.append(round(num))
print(rounded_numbers)
