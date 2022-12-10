def finds_palindrome_numbers():
    palindrome_numbers = []
    for current_number in numbers_as_digits:
        if str(current_number) == str(current_number)[::-1]:
            palindrome_numbers.append(True)
        else:
            palindrome_numbers.append(False)
    return palindrome_numbers
numbers = input().split(", ")
numbers_as_digits = [int(item) for item in numbers]
res = finds_palindrome_numbers()
for i in res:
    print(f"{i}")




