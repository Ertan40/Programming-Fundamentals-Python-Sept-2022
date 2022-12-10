letters = {}
symbols = "".join(s for s in input().split()) # texttexttext

for letter in symbols:
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1

for char, occurrences in letters.items():
    print(f"{char} -> {occurrences}")
