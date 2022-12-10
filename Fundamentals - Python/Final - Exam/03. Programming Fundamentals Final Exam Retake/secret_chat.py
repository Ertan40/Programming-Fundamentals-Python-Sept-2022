message = input()
command = input()

while command != "Reveal":
    no_substring = False
    command = command.split(":|:") # ['Reverse', '!gnil'] or ['ChangeAll', 'V', '1'] or ['InterSpace', '5']
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        message = f"{message[:index]} {message[index:]}"

    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            removed = message.replace(substring, "", 1)
            list_substring = list(substring)
            reversed_list = list_substring[::-1]
            result = "".join(reversed_list)
            message = removed + result
        elif substring not in message:
            no_substring = True
            print("error")

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    if not no_substring:
        print(message)
    command = input()
print(f"You have a new text message: {message}")
