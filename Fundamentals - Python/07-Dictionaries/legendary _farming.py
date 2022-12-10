items = {"shards": 0, "fragments": 0, "motes": 0}
item_is_obtained = False
command = input().split()

while not item_is_obtained:
    for index in range(0, len(command), 2):
        key = command[index+1].lower()
        quantity = int(command[index])
        if key not in items.keys():
            items[key] = 0
        items[key] += quantity
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items[key] -= 250
            item_is_obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items[key] -= 250
            item_is_obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items[key] -= 250
            item_is_obtained = True
        if item_is_obtained:
            break
    if item_is_obtained:
        break
    command = input().split()
for key, quantity in items.items():
    print(f"{key}: {quantity}")

