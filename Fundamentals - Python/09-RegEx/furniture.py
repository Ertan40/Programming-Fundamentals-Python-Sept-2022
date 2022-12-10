import re
pattern = r">>([A-Za-z]+)<<(\d+.*)!(\d)"
bought_furniture = []
total_price = 0
command = input()

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture_name, price, quantity = match.groups()
        bought_furniture.append(furniture_name)
        total_price += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture_name in bought_furniture:
    print(furniture_name)
print(f"Total money spend: {total_price:.2f}")