command = input()
cities_resources = {} # {'Tortuga': [345000, 1250], 'Santo Domingo': [240000, 630], 'Havana': [410000, 1100]}
while command != "Sail":
    command = command.split("||")
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city in cities_resources:
        cities_resources[city][0] += population
        cities_resources[city][1] += gold
        command = input()
        continue
    cities_resources[city] = [population, gold]
    command = input()

command = input()
while command != "End":
    command = command.split("=>")
    action = command[0]
    if action == "Plunder":
        town, killed_people, stolen_gold = command[1], int(command[2]), int(command[3])
        dead_people, gold_attained = 0, 0
        if cities_resources[town][0] >= killed_people and cities_resources[town][1] >= stolen_gold:
            dead_people, gold_attained = killed_people, stolen_gold
        if cities_resources[town][0] < killed_people:
            dead_people = cities_resources[town][0]
        if cities_resources[town][1] < stolen_gold:
            gold_attained = cities_resources[town][1]
        print(f"{town} plundered! {gold_attained} gold stolen, {dead_people} citizens killed.")
        cities_resources[town][0] -= dead_people
        cities_resources[town][1] -= gold_attained
        if cities_resources[town][0] <= 0 or cities_resources[town][1] <= 0:
            del cities_resources[town]
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        city, gold_increased = command[1], int(command[2])
        if gold_increased < 0:
            print("Gold added cannot be a negative number!")
            command = input()
            continue
        cities_resources[city][1] += gold_increased
        print(f"{gold_increased} gold added to the city treasury. {city} now has {cities_resources[city][1]} gold.")
    command = input()
if cities_resources:
    print(f"Ahoy, Captain! There are {len(cities_resources)} wealthy settlements to go to:")
    for town in cities_resources:
        print(f"{town} -> Population: {cities_resources[town][0]} citizens, Gold: {cities_resources[town][1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")