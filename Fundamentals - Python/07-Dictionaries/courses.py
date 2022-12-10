registered_users = {}
data = input().split(" : ") # ['Programming Fundamentals', 'John Smith']

while data[0] != "end":
    course_name = data[0]
    student_name = data[1]
    if course_name not in registered_users:
        registered_users[course_name] = [student_name]
    else:
        registered_users[course_name].append(student_name)
    data = input().split(" : ")

for course_name, student_name in registered_users.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {student}")

# courses_information = dict()
#
# def main():
#     command = input()
#     while command != "end":
#         command = command.split(" : ")
#         course = command[0]
#         student_name = command[1]
#         user_registration(course, student_name)
#         command = input()
#     print_result()
#
#
# def user_registration(course, student):
#     if course not in courses_information:
#         courses_information[course] = []
#     courses_information[course].append(student)
#
#
# def print_result():
#     for course in courses_information:
#         print(f"{course}: {len(courses_information[course])}")
#         for student in courses_information[course]:
#             print(f"-- {student}")
#
#
# main()