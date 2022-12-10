days = int(input())
players = int(input())
energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
water = water_per_day_per_person * players * days
food = food_per_day_per_person * players * days
energy_left = True

for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        energy_left = False
        break
    if day % 2 == 0:
        energy += energy * 0.05
        water -= water * 0.3
    if day % 3 == 0:
        energy += energy * 0.1
        food -= food / players

if energy_left:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")

else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")

