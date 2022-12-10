force_side_dict = {}
command = input()

while command != "Lumpawaroo":
    if " | " in command:
        splitted_command = command.split(" | ") # ['Light', 'Peter']
        force_side = splitted_command[0]
        force_user = splitted_command[1]
        present = False
        for value in force_side_dict.values():
            if force_user in value: # value is list!!!
                present = True
                break
        if not present:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)

    elif " -> " in command:
        splitted_command = command.split(" -> ")
        force_user = splitted_command[0]
        force_side = splitted_command[1]
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = [force_user]
        else:
            force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, force_user in force_side_dict.items():
    if len(force_user) > 0:
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for user in force_user:
            print(f"! {user}")