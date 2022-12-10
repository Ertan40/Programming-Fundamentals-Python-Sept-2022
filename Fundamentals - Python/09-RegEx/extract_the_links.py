import re

line = input()
pattern = r"\b(www.)([a-zA-Z0-9\-]+)((\.)([a-zA-Z+])+)+"
        # "(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
valid_list = []

while line:
    matches = re.search(pattern, line)
    if matches:
        valid_list.append(matches.group(0))
    line = input()
for valid in valid_list:
    print(valid)

