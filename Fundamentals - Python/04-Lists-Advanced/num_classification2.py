def finds_positive(numbers):
        return [num for num in numbers if int(num) >= 0]
def finds_negative(numbers):
        return [num for num in numbers if int(num) < 0]
def finds_even(numbers):
        return [num for num in numbers if int(num) % 2 == 0]
def finds_odd(numbers):
        return [num for num in numbers if int(num) % 2 != 0]

numbers_as_string = input().split(", ")
print(f"Positive: {', '.join(finds_positive(numbers_as_string))}")
print(f"Negative: {', '.join(finds_negative(numbers_as_string))}")
print(f"Even: {', '.join(finds_even(numbers_as_string))}")
print(f"Odd: {', '.join(finds_odd(numbers_as_string))}")