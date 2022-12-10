initial_rooms = input().split("|") # ['rat 10', 'bat 20', 'potion 10', 'rat 10', 'chest 100','boss 70', 'chest 1000']
health = 100
bitcoins = 0
room_tracker = 0
for items in initial_rooms:
    command_and_number = items.split() # ['chest', '1000']
    command = command_and_number[0] # chest
    number = int(command_and_number[1])  # 1000
    room_tracker += 1
    if command == "potion":
        if health + number < 100:
            number = number
        else:
            number = (100 - health)
        health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    elif command != "potion" or command != "chest":
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_tracker}")
            break
if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


