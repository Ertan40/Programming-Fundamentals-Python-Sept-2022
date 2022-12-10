text = input()

for index in range(len(text)):
    if text[index] == ":":
        print(f":{text[index +1]}")


# text = input()
# emo_finder = []

# for index in range(len(text)):
#     if text[index] == ":":
#         emo_finder.append(text[index])
#         emo_finder.append(text[index + 1])
# string = "".join(emo_finder)
#
# for i in range(1, len(string), 2):
#     print(f":{string[i]}")


