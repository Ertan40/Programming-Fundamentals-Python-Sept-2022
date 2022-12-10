cards = input().split(", ")
commands = int(input())

for c in range(1, commands + 1):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        card_name = command[1]
        if card_name not in cards:
            cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif action == "Remove":
        card_name = command[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(command[1])
        if 0 <= index < len(cards):
            del cards[index]
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action == "Insert":
        index = int(command[1])
        card_name = command[2]
        if 0 <= index < len(cards) and card_name in cards:
            print("Card is already added")
        elif 0 <= index < len(cards):
            cards.insert(index, card_name)
            print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(cards))