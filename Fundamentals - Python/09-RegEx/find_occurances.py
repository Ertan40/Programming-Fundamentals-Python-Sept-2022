import re
sentences = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"
matches = re.findall(pattern, sentences, flags=re.IGNORECASE)
print(len(matches))
