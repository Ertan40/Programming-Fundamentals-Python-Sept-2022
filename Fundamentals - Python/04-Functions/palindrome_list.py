numbers = input().split(", ") # [123, 323, 421, 121]
numbers_as_digits = [int(item) for item in numbers] # ['123', '323', '421', '121']
palindrome = []
non_palindrome = []
for current_number in numbers_as_digits:
    if str(current_number) == str(current_number)[::-1]:
        palindrome.append(current_number)
    else:
        non_palindrome.append(current_number)
print(palindrome)
print(non_palindrome)
# numbers = input()
# if str(numbers) == str(numbers[::-1]):
#     print(numbers)



