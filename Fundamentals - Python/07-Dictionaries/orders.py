orders = {}
command = input()

while command != "buy":
    current_products = command.split() # ['Beer', '2.20', '100']
    product = current_products[0]
    price = float(current_products[1])
    quantity = int(current_products[2])
    if product not in orders:
        orders[product] = [price, quantity]
    elif product in orders:
        orders[product][1] += quantity
        if price != orders[product][0]:
            orders[product][0] = price
    command = input()
for product in orders:
    total_price = orders[product][0] * orders[product][1]
    print(f"{product} -> {total_price:.2f}")