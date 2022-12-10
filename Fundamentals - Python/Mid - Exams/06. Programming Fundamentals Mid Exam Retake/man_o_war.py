status_pirate_ship = [int(j) for j in input().split(">")] # [12, 13, 11, 20, 66]
status_war_ship = [int(i) for i in input().split(">")] # [12, 22, 33, 44, 55, 32, 18]
max_health = int(input())
is_sunken = False
command = input().split() # ['Fire', '2', '11']
while command[0] != "Retire":
    action = command[0]
    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_war_ship):
            status_war_ship[index] -= damage
            if status_war_ship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                is_sunken = True
                break
    elif action == "Defend":
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx < len(status_pirate_ship) and 0 <= end_idx < len(status_pirate_ship):
            status_pirate_ship[start_idx:end_idx + 1] = [ship - damage for ship in status_pirate_ship[start_idx:end_idx +1]]
            sunken_pirate_ship_checker = [i for i in status_pirate_ship[start_idx:end_idx + 1] if i <= 0]
            if sunken_pirate_ship_checker:
                print("You lost! The pirate ship has sunken.")
                is_sunken = True
                break
    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate_ship):
            status_pirate_ship[index] += health
            if status_pirate_ship[index] >= max_health:
                status_pirate_ship[index] = max_health

    elif action == "Status":
        need_repair = max_health * 0.2
        sections_for_repair = [i for i in status_pirate_ship if i < need_repair]
        print(f"{len(sections_for_repair)} sections need repair.")
    command = input().split()

if not is_sunken and not command[0] != "Retire":
    print(f"Pirate ship status: {sum(status_pirate_ship)}")
    print(f"Warship status: {sum(status_war_ship)}")
