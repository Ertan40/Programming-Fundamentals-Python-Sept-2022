inventory = input().split(", ") # ['Iron', 'Wood', 'Sword']
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    if action == "Collect":
        item = command[1]
        if item not in inventory:
            inventory.append(item)
    elif action == "Drop":
        item = command[1]
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
           find_index = inventory.index(old_item)
           inventory.insert(find_index + 1, new_item)
    elif action == "Renew":
        item = command[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input()
print(", ".join(inventory))