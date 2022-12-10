words = input().split()
searched_palindrome = input()
palindrome_list = []

for current_word in words:
    if str(current_word) == str(current_word)[::-1]:
        palindrome_list.append(current_word)
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(searched_palindrome)} times")