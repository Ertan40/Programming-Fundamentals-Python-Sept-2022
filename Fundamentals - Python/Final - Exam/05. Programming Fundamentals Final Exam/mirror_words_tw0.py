import re
words = input()
pattern = r"(@|#){1}([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
mirror_words = []
total_pairs = 0
matches = re.findall(pattern, words)
# [('#', 'poOl', 'loOp'), ('#', 'Part', 'traP'), ('@', 'leveL', 'Level'), ('@', 'pack', 'ckap'), ('#', 'sAw', 'wAs')]
for word in matches:
    if word[1] == word[2][::-1]:
        mirror_words.append(f"{word[1]} <=> {word[2]}")
# print(mirror_words)   ['Part <=> traP', 'leveL <=> Level', 'sAw <=> wAs']
if len(matches) > 0 and len(mirror_words) > 0:
    print(f"{len(matches)} word pairs found!")
    print(f"The mirror words are: \n{', '.join(mirror_words)}")
elif len(matches) == 0 and len(mirror_words) == 0:
    print("No word pairs found!")
    print("No mirror words!")
elif len(matches) > 0 and len(mirror_words) == 0:
    print(f"{len(matches)} word pairs found!")
    print("No mirror words!")

# ('#', 'poOl', 'loOp')
# ('#', 'Part', 'traP')
# ('@', 'leveL', 'Level')
# ('@', 'pack', 'ckap')
# ('#', 'sAw', 'wAs')