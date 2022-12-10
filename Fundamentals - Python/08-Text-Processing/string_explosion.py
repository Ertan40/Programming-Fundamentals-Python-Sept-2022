some_text = input()
strength = 0
final_text = ""
for index in range(len(some_text)):
    if some_text[index] == ">":
        final_text += some_text[index]
        strength += int(some_text[index+1])
    elif some_text[index] != ">" and strength > 0:
        strength -= 1
    else:
        final_text += some_text[index]
print(final_text)