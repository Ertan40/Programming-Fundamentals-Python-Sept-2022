characters = input().split(", ") # ['a', 'b', 'c', 'a']

my_dict = {char:ord(char) for char in characters}
print(my_dict)

