text = input()

while text != "end":
    my_list = list(text)
    into_string = ''.join(my_list[::-1])

    print(f"{text} = {into_string}")
    text = input()

