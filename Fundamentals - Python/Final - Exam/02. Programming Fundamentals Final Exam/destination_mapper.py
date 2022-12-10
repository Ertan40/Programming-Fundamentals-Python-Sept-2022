import re

places = input()
valid_pattern = r"(=|\/)([A-ZA-Za-z]{2,})\1"
valid_locations = []
travel_points = 0
matches = re.finditer(valid_pattern, places)

for match in matches:
    destination = re.split("=|\/", match.group())[1]
    valid_locations.append(destination) # ['Hawai', 'Cyprus']
    travel_points += len(destination) # 11

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {travel_points}")

# if matches:
#     print(f"Destinations: {matches[0][1]}, {matches[0][3]}")
#     print(f"Travel Points: {len(matches[0][1]) + len(matches[0][3])}")
# else:
#     print(f"Destinations: ")
#     print(f"Travel Points: {0}")




