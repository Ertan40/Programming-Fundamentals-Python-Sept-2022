number = int(input())
plant_dict = {}

for _ in range(number):
    plants = input().split("<->")
    plant = plants[0]
    rarity = int(plants[1])
    if plant not in plant_dict:
        plant_dict[plant] = {"rarity": rarity, "rating": []}
    else:
        plant_dict[plant]["rarity"] += rarity
    # {'Arnoldii': {'rarity': 4, 'rating': []}, 'Woodii': {'rarity': 7, 'rating': []},
    #  'Welwitschia': {'rarity': 2, 'rating': []}}

command = input().split(": ") # ['Rate', ' Woodii - 10 ']
print(command[1])

while command[0] != "Exhibition":
    data = command[1].split(" - ")
    plant = data[0]
    if plant not in plant_dict:
        print("error")
        command = input().split(": ")
        continue
    if command[0] == "Rate":
        rating = int(data[1])  # Woodi, 10
        plant_dict[plant]["rating"].append(rating)
        # {'Arnoldii': {'rarity': 4, 'rating': []}, 'Woodii': {'rarity': 7, 'rating': [10]},
        # /'Welwitschia': {'rarity': 2, 'rating': []}}

    elif command[0] == "Update":
        new_rarity = int(data[1])
        plant_dict[plant]["rarity"] = new_rarity

    elif command[0] == "Reset":
        plant_dict[plant]["rating"] = []
    command = input().split(": ")

print("Plants for the exhibition:")
for plant in plant_dict:
    rating = 0
    rarity = plant_dict[plant]["rarity"]
    if len(plant_dict[plant]["rating"]):
        rating = sum(plant_dict[plant]["rating"]) / len(plant_dict[plant]["rating"])
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")

# for dict_el in plant_dict:
#     if len(plant_dict[dict_el]["rating"]) > 0 and sum(plant_dict[dict_el]["rating"]) >0:
#         average_rating = sum(plant_dict[dict_el]["rating"]) / len(plant_dict[dict_el]["rating"])
#     else:
#         average_rating = 0
#     rarity = plant_dict[dict_el]["rarity"]
#     print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")


# for plant, rating in plant_dict.items():
#     print(f"{plant}; Rarity: {rating[0]}; Rating: {rating[1]}")