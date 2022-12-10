command = input()
total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

while command != "special" and command != "regular":
    current_command = float(command)
    if current_command < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price_without_taxes += current_command
    command = input()

total_amount_of_taxes += total_price_without_taxes * 0.2
total_price_with_taxes = total_price_without_taxes + (total_price_without_taxes * 0.2)

if command == "special":
    total_price_with_taxes = total_price_with_taxes - (total_price_with_taxes * 0.1)
if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer! \nPrice without taxes: {total_price_without_taxes:.2f}$\
     \nTaxes: {total_amount_of_taxes:.2f}$ \n----------- \nTotal price: {total_price_with_taxes:.2f}$")

