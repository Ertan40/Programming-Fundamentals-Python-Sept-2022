waiting_people = int(input())
current_state_of_the_lift = [int(i) for i in input().split()] # [0, 0, 0, 0]

for current in range(len(current_state_of_the_lift)):
    if waiting_people > 3:
        current_number_of_people = abs(4 - current_state_of_the_lift[current])
        waiting_people -= current_number_of_people
        current_state_of_the_lift[current] += current_number_of_people
    else:
        current_state_of_the_lift[current] += waiting_people
        waiting_people = 0
final_state = [str(i) for i in current_state_of_the_lift]
if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(" ".join(final_state))
elif waiting_people <= 0:
    print("The lift has empty spots!")
    print(" ".join(final_state))
elif waiting_people == 0 and sum(current_state_of_the_lift) == len(current_state_of_the_lift) * 4:
    print(" ".join(final_state))
