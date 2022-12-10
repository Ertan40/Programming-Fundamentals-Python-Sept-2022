targets = input().split(" ")
command = input()
targets_as_digits = [int(item) for item in targets] # [52, 74, 23, 44, 96, 110]
# targets = list(map(lambda x: int(x), input().split()))
while command != "End":
    command = command.split(" ")
    current_command = command[0]
    idx = int(command[1])
    value = int(command[2])
    if current_command == "Shoot":
        if 0 <= idx < len(targets_as_digits):
            if targets_as_digits[idx] - value <= 0:
                targets_as_digits.remove(targets_as_digits[idx])
            else:
                targets_as_digits[idx] -= value
    elif current_command == "Add":
        if 0 <= idx < len(targets_as_digits):
            targets_as_digits.insert(idx, value)
        else:
            print("Invalid placement!")
    elif current_command == "Strike":
        if 0 <= idx < len(targets_as_digits) and 0 <= idx - value < len(targets_as_digits)\
            and 0 <= idx  + value < len(targets_as_digits):

            del targets_as_digits[idx - 1:idx + 2]
        else:
            print("Strike missed!")
    command = input()
print("|".join([str(item) for item in targets_as_digits]))
# format_print = '|'.join(list(map(lambda x: str(x), targets)))
# print(format_print)