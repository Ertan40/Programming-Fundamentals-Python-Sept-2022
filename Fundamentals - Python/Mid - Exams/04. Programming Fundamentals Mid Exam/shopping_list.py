groceries = input().split("!") # ['Tomatoes', 'Potatoes', 'Bread']
command = input().split() # ['Unnecessary', 'Milk']

while command[1] != "Shopping!":
    action = command[0]
    if action == "Urgent":
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif action == "Unnecessary":
        item = command[1]
        if item in groceries:
            groceries.remove(item)

    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            index_old_item = groceries.index(old_item)
            groceries.insert(index_old_item, new_item)
            groceries.pop(index_old_item + 1)

    elif action == "Rearrange":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input().split()

print(", ".join(groceries))