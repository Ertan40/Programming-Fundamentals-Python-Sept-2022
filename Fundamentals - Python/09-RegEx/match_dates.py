import re
dates = input()

search_pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
result = re.findall(search_pattern, dates)

for data in result:
    print(f"Day: {data[0]}, Month: {data[2]}, Year: {data[3]}")