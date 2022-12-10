number_of_the_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus_points = 0
max_student_attendances = 0
for current_student in range(1, number_of_the_students + 1):
    student_attendances = int(input())
    total_bonus = student_attendances / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
    if student_attendances > max_student_attendances:
        max_student_attendances = student_attendances
print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {max_student_attendances} lectures.")


# total = 19 / 25 * (5 + 30)
