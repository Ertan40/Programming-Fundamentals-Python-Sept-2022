number_of_people = int(input())
capacity = int(input())
number = int(number_of_people / capacity)
if number_of_people % capacity != 0:
    number += 1
print(number)