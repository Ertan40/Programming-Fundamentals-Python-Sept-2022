command = input()
my_list = [0] * 10
while command != "End":
    tokens = command.split("-") # ['2', 'Walk the dog']
    importance = int(tokens[0]) - 1
    note = tokens[1]
    my_list.pop(importance)
    print(my_list)
    my_list.insert(importance, note)
    command = input()

delete_zeros = [item for item in my_list if item != 0]
print(delete_zeros)
