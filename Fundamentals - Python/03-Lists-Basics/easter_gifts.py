gifts = input().split() #['Sweets', 'Cozonac', 'Clothes', 'Flowers', 'Wine', 'Clothes', 'Eggs', 'Clothes']
command = input()
while command != "No Money":
    tokens = command.split(" ") #first_command: ['OutOfStock', 'Eggs'] 2nd: ['Required', 'Spoon', '2']
                                       # \ 3rd: ['JustInCase', 'ChocolateEgg']
    if tokens[0] == "OutOfStock":
        gift = tokens[1]
        for i in range(len(gifts)):
           if gifts[i] == gift:
               gifts[i] = "None"
    elif tokens[0] == "Required":
        idx = int(tokens[2])
        if idx >= 0 and idx < len(gifts):
            gifts[idx] = tokens[1]
    elif tokens[0] == "JustInCase":
        gifts[-1] = tokens[1]
    command = input()
result = []
for gift in gifts:
    if gift != "None":
        result.append(gift)
print(" ".join(result))


