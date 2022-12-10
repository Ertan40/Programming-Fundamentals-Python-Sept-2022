sum_lists_as_strings = input().split(", ")
count_of_beggars = int(input())
index_counter = 0
offers = []
sum_lists_as_digits = []
# sum_lists_as_digits = [int(item) for item in sum_lists_as_strings]
for element in sum_lists_as_strings:
    sum_lists_as_digits.append(int(element))
while index_counter < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(index_counter, len(sum_lists_as_digits), count_of_beggars):
        sum_of_current_beggar += sum_lists_as_digits[current_index]
    index_counter += 1
    offers.append(sum_of_current_beggar)
print(offers)
