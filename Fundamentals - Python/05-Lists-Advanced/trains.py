number_of_wagons = int(input())
my_list = [0] * number_of_wagons
command = input()

while command != "End":
    tokens = command.split()
    key_word = tokens[0]
    if key_word == "add":
        num_of_people = int(tokens[1])
        my_list[-1] += num_of_people
    elif key_word == "insert":
        idx = int(tokens[1])
        number_of_people = int(tokens[2])
        my_list[idx] += number_of_people
    elif key_word == "leave":
        number_of_people = int(tokens[2])
        my_list[idx] -= number_of_people
    command = input()
print(my_list)