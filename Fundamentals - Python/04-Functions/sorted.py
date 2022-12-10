numbers = input().split()
numbers_as_digits = [int(num) for num in numbers]
result = sorted(numbers_as_digits)
print(result)