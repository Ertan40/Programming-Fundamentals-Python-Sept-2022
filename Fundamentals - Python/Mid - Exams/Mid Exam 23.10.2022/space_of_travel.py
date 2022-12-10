# Mid exam - final score : 90

titans = input().split("||") # ['Travel 10', 'Enemy 30', 'Repair 15', 'Titan']
amount_of_fuel = int(input())
amount_of_ammunition = int(input())

for item in titans:
    command = item.split() # ['Travel', '10']
    action = command[0] # Travel

    if action == "Travel":
        distance = int(command[1])
        if amount_of_fuel > 0:
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break
        amount_of_fuel -= distance
    elif action == "Enemy":
        enemy_armour = int(command[1])
        if amount_of_ammunition >= enemy_armour:
            amount_of_ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        elif amount_of_ammunition < enemy_armour:
            amount_of_fuel -= enemy_armour * 2
            print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif action == "Repair":
        ammunition_and_fuel = int(command[1])
        amount_of_fuel += ammunition_and_fuel
        current = (2 * ammunition_and_fuel)
        amount_of_ammunition += current
        print(f"Ammunitions added: {current}.")
        print(f"Fuel added: {ammunition_and_fuel}.")
    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break




