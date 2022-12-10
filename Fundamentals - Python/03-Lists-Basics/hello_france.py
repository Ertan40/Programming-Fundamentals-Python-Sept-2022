collection_of_items = input().split("|") # ['Clothes->43.30', 'Shoes->25.25', 'Clothes->36.52', 'Clothes->20.90']
budget = float(input())
ticket_cost = 150
initial_budget = budget
increased_price = 0
new_prices = []
for items in collection_of_items:
    product = items.split("->") # ['Accessories', '15.60']
    type_of_product = product[0] # Accessories
    price = float(product[1]) # 15.6
    if budget >= price:
        if type_of_product == "Clothes":
            if price <= 50.00:
                budget -= price
                increased_price = price * 1.4
                new_prices.append(increased_price)
        elif type_of_product == "Shoes":
            if price <= 35.00:
                budget -= price
                increased_price = price * 1.4
                new_prices.append(increased_price)
        elif type_of_product == "Accessories":
            if price <= 20.50:
                budget -= price
                increased_price = price * 1.4
                new_prices.append(increased_price)
profit = (sum(new_prices) - initial_budget) + budget
for prices in new_prices:
    print(f"{prices:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if budget + sum(new_prices) >= ticket_cost:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")


