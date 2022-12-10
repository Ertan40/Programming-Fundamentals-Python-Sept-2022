string = input()  # Hawai::Cyprys-Greece
command = input()

while command != "Travel":
    command = command.split(":") #['Add Stop', '7', 'Rome']['Remove Stop', '11', '16']['Switch', 'Hawai', 'Bulgaria']
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        dif_string = command[2]
        if index <= len(string):
            string = string[:index] + dif_string + string[index:]
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index and end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
    print(string)
    command = input()
print(f"Ready for world tour! Planned stops: {string}")