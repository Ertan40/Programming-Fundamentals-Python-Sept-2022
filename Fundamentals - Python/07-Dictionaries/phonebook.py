phone_book = {}
command = input()

while "-" in command:
    numbers = command.split("-") # ['Adam', '0888080808']
    name = numbers[0]
    number = numbers[1]
    phone_book[name] = number # {'Adam': '+359888001122', 'Ralf': '666', 'George': '5559393',
    # \'Silvester': '02/987665544'}
    command = input()

for name in range(int(command)):
    searched_name = input()
    if searched_name in phone_book.keys():
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


