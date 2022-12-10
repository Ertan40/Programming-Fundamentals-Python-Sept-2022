# numbers = input().split()
# numbers_as_digits = [int(num) for num in numbers if int(num) % 2 == 0]
# print(numbers_as_digits)

numbers = input().split()
numbers_as_digits = [int(num) for num in numbers]
result = list(filter(lambda a: a % 2 == 0, numbers_as_digits))
print(result)