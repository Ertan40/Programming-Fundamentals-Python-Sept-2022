chest = input().split("|") # ['Gold', 'Silver', 'Bronze', 'Medallion', 'Cup']
command = input().split() # ['Loot', 'Wood', 'Gold', 'Coins']

while command[0] != "Yohoho!":
    action = command[0]
    if action == "Loot":
        total_items = command[1::] # ['Wood', 'Gold', 'Coins']
        for t in total_items:
            if t not in chest:
                chest.insert(0, t) # ['Pistol', 'Coins', 'Wood', 'Gold', 'Silver', 'Bronze', 'Medallion', 'Cup']

    elif action == "Drop":
        index = int(command[1])
        if index <= len(chest):
            deleted = chest.pop(index)
            chest.append(deleted) # ['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze', 'Medallion', 'Cup', 'Gold']

    elif action == "Steal":
        last_count = int(command[1])
        print(", ".join(chest[-last_count:])) # ['Medallion', 'Cup', 'Gold']
        del chest[-last_count:] # ['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze']
    command = input().split()

if len(chest) > 0:
    remained_items = [len(item) for item in chest]
    remained_items_as_digits = [int(item) for item in remained_items]
    average_gain = sum(remained_items_as_digits) / len(chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
