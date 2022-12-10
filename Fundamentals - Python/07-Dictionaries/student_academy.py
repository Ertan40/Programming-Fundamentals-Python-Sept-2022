pair_of_rows = int(input())
grades = {}

for data in range(pair_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in grades.keys():
        grades[student_name] = [grade]
    else:
        grades[student_name] += [grade]
# print(grades) - {'John': [5.5, 4.5], 'Alice': [6.0, 3.0], 'George': [5.0]}

for name, grade in grades.items():
    average_grade = sum(grade)/len(grade)
    if average_grade >= 4.50:
         print(f"{name} -> {average_grade:.2f}")

