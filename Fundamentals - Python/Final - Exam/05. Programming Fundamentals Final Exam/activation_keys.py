activation_key = input()
raw_activation_key = activation_key
command = input()
flag = False
while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in activation_key:
            flag = True
            print(f"{activation_key} contains {substring}")
        else:
            flag = True
            print("Substring not found!")
    elif action == "Flip":
        upper_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if upper_lower == "Upper":
            flag = True
            activation_key = activation_key[:start_index]+activation_key[start_index:end_index].upper()\
                             + activation_key[end_index:]
            print(activation_key)
        elif upper_lower == "Lower":
            flag = True
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower()\
                             + activation_key[end_index:]
            print(activation_key)
    elif action == "Slice":
        flag = True
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()
if flag:
    print(f"Your activation key is: {activation_key}")




