def odd_and_even_sum(single_number):
    single_number_as_digits = [int(num) for num in single_number]
    my_list_odd = []
    my_list_even = []
    for current_number in single_number_as_digits:
        if current_number % 2 == 0:
            my_list_even.append(current_number)
        else:
            my_list_odd.append(current_number)
    sum_of_odd_digits = sum(my_list_odd)
    sum_of_even_digits = sum(my_list_even)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

single_number = input()
result = odd_and_even_sum(single_number)
print(result)
