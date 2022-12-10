password = input()
password_ = ''
command = input()
while command != "Done":
    command = command.split()
    action = command[0]
    flag = False
    if action == "TakeOdd":
        for index in range(len(password)):
            if index % 2 != 0: # password = password[1::2] for odd password[0::2] for even
                password_ += password[index]
        password = password.replace(password, "")
        password = password + password_
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index+length:]
    if action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            flag = True
            print(f"Nothing to replace!")
    if not flag:
        print(password)
    command = input()
print(f"Your password is: {password}")