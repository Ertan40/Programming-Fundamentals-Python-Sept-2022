number_of_cars = int(input())
cars_dict = {}
max_allowed_fuel = 75
for _ in range(number_of_cars):
    data = input().split("|")
    car, mileage, fuel = data[0], data[1], data[2]
    cars_dict[car] = [int(mileage), int(fuel)]
    # {'Audi A6': ['38000', '62 '], 'Mercedes CLS': ['11000', '35 '], 'Volkswagen Passat CC': ['45678', '5 ']}
command = input()
while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars_dict[car][1] >= fuel:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars_dict[car][0] > 100000:
            del cars_dict[car]
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        car, fuel = command[1], int(command[2])
        current_fuel = cars_dict[car][1]
        cars_dict[car][1] += fuel
        if cars_dict[car][1] > max_allowed_fuel:
            print(f"{car} refueled with {max_allowed_fuel - current_fuel} liters")
            cars_dict[car][1] = max_allowed_fuel
        elif cars_dict[car][1] <= max_allowed_fuel:
            print(f"{car} refueled with {fuel} liters")
    if action == "Revert":
        car, kilometers = command[1], int(command[2])
        cars_dict[car][0] -= kilometers
        if cars_dict[car][0] <= 10000:
            cars_dict[car][0] = 10000
            command = input()
            continue
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()
for car, info in cars_dict.items():
    print(f"{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.")