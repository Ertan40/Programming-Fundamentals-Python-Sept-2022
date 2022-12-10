numbers = input().split(" ")
finish_line = len(numbers) // 2

for racer in range(finish_line):
    left_racer = numbers[0:finish_line]
    right_racer = numbers[finish_line+1::]
    left_racer_score = 0
    right_racer_score = 0
left_racer_as_digits = [int(item) for item in left_racer]
right_racer_as_digits = [int(item) for item in right_racer]
right_racer_as_digits.reverse()
for score in left_racer_as_digits:
    if score != 0:
        left_racer_score += score
    else:
        left_racer_score = left_racer_score * 0.8
for score in right_racer_as_digits:
    if score != 0:
        right_racer_score += score
    else:
        right_racer_score = right_racer_score * 0.8

if left_racer_score < right_racer_score:
    print(f"The winner is left with total time: {left_racer_score:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_score:.1f}")

