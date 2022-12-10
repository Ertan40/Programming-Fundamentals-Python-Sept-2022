def return_single_string(first_char, second_char):
    first_into_number = ord(first_char)
    second_into_number = ord(second_char)
    my_list = []
    for i in range(first_into_number+1, second_into_number):
        my_list.append(chr(i))
    return " ".join(my_list)

first_input = input()
second_input = input()
print(return_single_string(first_input, second_input))

