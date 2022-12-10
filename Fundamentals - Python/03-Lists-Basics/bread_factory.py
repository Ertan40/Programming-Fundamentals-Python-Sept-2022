working_day_events = input().split("|") #['rest-2', 'order-10', 'eggs-100', 'rest-10']
factory_is_closed = False
total_energy = 100
total_coins = 100
for event in working_day_events:
    event_items = event.split("-") # ['rest', '10']
    event_name = event_items[0] # rest
    event_value = int(event_items[1]) # 10
    if event_name == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_name == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            factory_is_closed = True
            break
if not factory_is_closed:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

