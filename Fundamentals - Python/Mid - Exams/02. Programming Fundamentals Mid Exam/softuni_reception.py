first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())
all_employees_per_hour = first_employee + second_employee + third_employee
hour_counter = 0
while number_of_students > 0:
      number_of_students -= all_employees_per_hour
      hour_counter += 1
      if hour_counter % 4 == 0 and hour_counter != 0:
          hour_counter += 1
print(f"Time needed: {hour_counter}h.")