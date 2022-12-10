def finds_perfect_num(some_number):
    perfect_nums = []
    for current_num in range(1, some_number):
        if number % current_num == 0:
            perfect_nums.append(current_num)
    if sum(perfect_nums) == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
res = finds_perfect_num(number)
print(res)
