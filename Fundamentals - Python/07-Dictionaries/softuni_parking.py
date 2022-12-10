number_of_commands = int(input())
registered = {}

for c in range(number_of_commands):
    command = input().split() # ['register', 'John', 'CS1234JS']
    action = command[0]
    if action == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in registered:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        username = command[1]
        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered[username]
for username, license_plate_number in registered.items():
    print(f"{username} => {license_plate_number}")
