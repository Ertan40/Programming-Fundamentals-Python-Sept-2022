# elements = input().split(" ")
# bakery = {elements[i]:int(elements[i + 1]) for i in range(0, len(elements), 2)}
# print(bakery)

elements = input().split(" ")
bakery = {} # bakery = dict()

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    bakery[key] = int(value)

print(bakery)