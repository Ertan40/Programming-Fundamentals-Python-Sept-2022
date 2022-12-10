import re

text = input()
pattern = r"(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.finditer(pattern, text)
total_calories = 0
print_result = ""
for match in matches:
    print_result += f"Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}\n"
    total_calories += int(match.group(4))

days = total_calories / 2000
print(f"You have food to last you for: {int(days)} days!")
print(print_result)




##Bread#19/03/21#4000
# |Apples|08/10/20|200
# |Carrots|06/08/20|500