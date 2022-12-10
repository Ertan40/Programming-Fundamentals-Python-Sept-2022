import re
line = input()
pattern = r"\d+"
while True:
    if line:
        result = re.findall(pattern, line)
        if result:
            print(" ".join(result), end=" ")
    else:
        break
    line = input()

