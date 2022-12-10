number_of_heroes = int(input())
points = {}
max_hit_points = 100
max_mana_points = 200
for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    points[hero_name] = [int(hit_points), int(mana_points)] # {'Solmyr': ['85', '120'], 'Kyrre': ['99', '50']}

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if points[hero_name][1] >= mp_needed:
            points[hero_name][1] -= mp_needed # mana_points_left = points[hero_name][1] - mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {points[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        points[hero_name][0] -= damage # current_hp = points[hero_name][0] - damage
        if points[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {points[hero_name][0]} HP left!" )
        else:
            del points[hero_name]
            print(f"{hero_name} has been killed by {attacker}!" )
    elif action == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        points[hero_name][1] += amount # added
        if points[hero_name][1] <= max_mana_points:
            print(f"{hero_name} recharged for {amount} MP!")
        elif points[hero_name][1] > max_mana_points:
            difference = points[hero_name][1] - max_mana_points
            points[hero_name][1] = 200 # max value is 200!!
            print(f"{hero_name} recharged for {amount - difference} MP!")
    elif action == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        points[hero_name][0] += amount # added
        if points[hero_name][0] <= max_hit_points:
            print(f"{hero_name} healed for {amount} HP!")
        elif points[hero_name][0] > max_hit_points:
            difference = points[hero_name][0] - max_hit_points
            points[hero_name][0] = 100 # max value is 100!!
            print(f"{hero_name} healed for {amount - difference} HP!")

    command = input()
result = ""
for hero in points:
    hp = points[hero][0]
    mp = points[hero][1]
    result += f"{hero}\n  HP: {hp}\n  MP: {mp}\n"
print(result)

# result = ""
# for hero, point in points.items():
#     result += f"{hero}\n  HP: {int(point[0])}\n  MP: {int(point[1])}\n"
#
# print(result)




