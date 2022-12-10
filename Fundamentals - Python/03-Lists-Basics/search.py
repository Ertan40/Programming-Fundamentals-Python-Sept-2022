n = int(input())
word = input()
all_words = []
for current_word in range(n):
    current_word = input()
    all_words.append(current_word)
print(all_words)
for i in range(len(all_words) -1, -1, -1):
    element = all_words[i]
    if word not in element:
        all_words.remove(element)
print(all_words)




