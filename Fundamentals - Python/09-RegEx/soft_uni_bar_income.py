import re
command = input()
income = 0
while command != "end of shift":
    current_command = command
    pattern = r'%(?P<name>[A-Z][a-z]*)%[^\$^\|^%^\.]*<(?P<product>\w+)>[^\$^\|^%^\.]*\|(?P<count>-?\d+)\|\D*(?P<price>-?\d+(?:(\.\d+)?))\$.*'
    matches = re.match(pattern, current_command)
    if matches:
        total_price = float(matches.group(3)) * float(matches.group(4))
        income += total_price
        print(f"{matches.group(1)}: {matches.group(2)} - {total_price:.2f}")
        # print(matches.group()  # % George % < Croissant > | 2 | 10.3$
                                # % Peter % < Gum > | 1 | 1.3$
                                # % Maria % < Cola > | 1 | 2.4$
    command = input()
print(f"Total income: {income:.2f}")