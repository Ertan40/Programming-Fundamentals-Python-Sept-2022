strings = input().split() # ['hi', 'abc', 'add']
result = ""

for word in strings:
    length = len(word)
    result += word * length

print(result)

# [print(s * len(s), end="") for s in input().split()]

# second way
