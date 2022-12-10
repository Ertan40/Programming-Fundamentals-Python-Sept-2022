initial_energy = int(input())
command = input()
counts_won_battles = 0
while command != "End of battle":
    current_command = int(command)
    if initial_energy < current_command:
        print(f"Not enough energy! Game ends with {counts_won_battles} won battles and {initial_energy} energy")
        break
    initial_energy -= current_command
    counts_won_battles += 1
    if counts_won_battles % 3 == 0:
        initial_energy += counts_won_battles
    command = input()

if not command != "End of battle":
    print(f"Won battles: {counts_won_battles}. Energy left: {initial_energy}")
