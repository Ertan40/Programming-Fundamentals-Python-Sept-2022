numbers = [int(i) for i in input().split()] # [10, 20, 30, 40, 50]
average_of_numbers = sum(numbers) / len(numbers)

if average_of_numbers == 1 or average_of_numbers == -1:
    print("No")
    exit()
nums_greater_than = [i for i in numbers if i > average_of_numbers]
nums_greater_than.sort(reverse=True)
if len(nums_greater_than) >= 5:
    less_than_five = nums_greater_than[:5]
    less_than_five_as_digits = [str(i) for i in less_than_five]
    print(" ".join(less_than_five_as_digits))
else:
    print(" ".join([str(i) for i in nums_greater_than]))