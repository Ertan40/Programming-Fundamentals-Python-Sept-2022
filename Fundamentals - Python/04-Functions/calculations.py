input_operator = input()
first_num = int(input())
second_num = int(input())
def solve(x, y, operator):

    if operator == "multiply":
        return (x * y)
    elif operator == "divide":
        return int(x / y)
    elif operator == "add":
        return (x + y)
    elif operator == "subtract":
        return (x - y)
print(solve(first_num, second_num, input_operator))
