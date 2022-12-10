word = input()
lowered_word = word.lower()
counter = 0
for i in ("sand", "water", "fish", "sun"):
    counter += lowered_word.count(i)
print(counter)
##answer two##
word = input()
lowered_word = word.lower()
print(lowered_word.count("sand") + lowered_word.count("water") + lowered_word.count("fish") + lowered_word.count("sun"))
