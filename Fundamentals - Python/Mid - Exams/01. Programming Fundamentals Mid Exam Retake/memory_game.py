elements = input().split() # ["1", "1", "2", "2", "3", "3", "4", "4", "5", "5"]
command = input().split()
moves_counter = 0
while command[0] != "end":
    first_index = int(command[0])
    second_index = int(command[1])
    moves_counter += 1
    if first_index == second_index or 0 > first_index or first_index >= len(elements)\
            or 0 > second_index or second_index >= len(elements):
        middle_of_elements = int(len(elements) // 2)
        elements.insert(middle_of_elements, f"-{moves_counter}a")
        elements.insert(middle_of_elements, f"-{moves_counter}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements = [item for item in elements if item != elements[first_index]]

    elif elements[first_index] != elements[second_index] and 0 <= first_index < len(elements):
        print(f"Try again!")

    if len(elements) <= 0:
        print(f"You have won in {moves_counter} turns!")
        break

    command = input().split()

if not command[0] != "end":
    print(f"Sorry you lose :(\n{' '.join(elements)}")
