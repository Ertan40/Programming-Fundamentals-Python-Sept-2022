houses = [int(i) for i in input().split("@")] # [10, 10, 10, 2]
command = input().split() # ['Jump', '1']
last_index = 0

while command[0] != "Love!":
    jump_command = command[0]
    length = int(command[1])
    jump = last_index + length
    if jump >= len(houses):
        jump = 0
    house = houses[jump] 
    if house == 0:
        print(f"Place {jump} already had Valentine's day.")
    else:
        houses[jump] -= 2
        if houses[jump] == 0:
            print(f"Place {jump} has Valentine's day.")
    last_index = jump

    command = input().split()
print(f"Cupid's last position was {last_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
# if not command[0] != "Love!":
else:
    print(f"Cupid has failed {len(houses) - houses.count(0)} places.")