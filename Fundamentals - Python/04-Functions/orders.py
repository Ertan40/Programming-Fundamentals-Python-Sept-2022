product = input()
quantity_of_product = int(input())

def total_price(quantity, order):
    if order == "coffee":
        return 1.50 * quantity
    elif order == "coke":
        return 1.40 * quantity
    elif order == "water":
        return 1.00 * quantity
    elif order == "snacks":
        return 2.00 * quantity

print(f"{total_price(quantity_of_product, product):.2f}")
