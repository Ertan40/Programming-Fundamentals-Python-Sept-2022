# while True:
#     number = float(input())
#     if 1 <= number <= 100:
#         print(f"The number {number} is between 1 and 100")
#         break
budget = int(input())
bought_product = 0
command = input()
while command != "End":
    product_price = int(command)
    bought_product += product_price
    if bought_product > budget:
        print("You went in overdraft!")
        break
    command = input()
if not command != "End":
    print("You bought everything needed.")