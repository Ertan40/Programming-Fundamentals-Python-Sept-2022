import re
emojis = input()
pattern = r"([0-9])|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})"
result = re.finditer(pattern, emojis)
cool_threshold = 1
emojis_dict = {}

for match in result:
    number = match.group()
    if number.isdigit():
        cool_threshold *= int(number)
    else:
        emojis_dict[number] = 0 # {'::Smiley::': 0}
        for ch in number:
            if ch != ":" and ch != "*":
                emojis_dict[number] += ord(ch)
                # {'::Smiley::': 627, '**Tigers**': 622, '::Mooning::': 727, '**Shy**': 308}
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_dict)} emojis found in the text. The cool ones are:")
for emoji, number in emojis_dict.items():
    if number >= cool_threshold:
        print(emoji)

