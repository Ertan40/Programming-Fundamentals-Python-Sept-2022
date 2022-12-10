number = input()
list_number = list(number)
list_number.sort(reverse=True)

turn_to_integer = [str(item) for item in list_number]
a_string = "".join(turn_to_integer)

res = int(a_string)
print(res)














