data = input()
result = ""
current_combination = ""
for index in range(len(data)):
    if index + 1 < len(data) and data[index].isdigit() and data[index+1].isdigit():
        current_combination = current_combination * int(data[index:index+2])
        result += current_combination
        current_combination = ""
    elif data[index].isdigit():
        current_combination = current_combination * int(data[index])
        result += current_combination
        current_combination = ""
    else:
        current_combination += data[index]

result = result.upper()
print(f"Unique symbols used: {len(set(result))}")
print(result)









