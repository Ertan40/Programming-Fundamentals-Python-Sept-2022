def factorial_division(some_number):
    for current_number in range(1, some_number):
        some_number *= current_number
    return some_number

number_one = int(input())
number_two = int(input())
first_number_factorial = factorial_division(number_one)
second_number_factorial = factorial_division(number_two)
res = first_number_factorial / second_number_factorial
print(f"{res:.2f}")
