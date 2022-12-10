data = {}
command = input().split(" -> ") # ['SoftUni', 'AA12345']

while command[0] != "End":
    company_name = command[0]
    employee_id = command[1]
    if company_name not in data.keys():
        data[company_name] = [employee_id]
    elif company_name in data.keys():
        if employee_id not in data[company_name]:
            data[company_name].append(employee_id)
    command = input().split(" -> ")

# print(data) - {'SoftUni': ['AA12345', 'CC12344'], 'Lenovo': ['XX23456'], 'Movement': ['DD11111']}
for company_name, employee_id in data.items():
    print(f"{company_name}")
    for id in employee_id:
        print(f"-- {id}")





