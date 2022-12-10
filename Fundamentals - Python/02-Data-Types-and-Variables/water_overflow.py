number_of_lines = int(input())
current_capacity = 0
for i in range(number_of_lines):
    current_water = int(input())
    current_capacity += current_water
    if current_capacity >= 255:
        print("Insufficient capacity!")
        current_capacity -= current_water
        continue
print(f"{current_capacity}")

