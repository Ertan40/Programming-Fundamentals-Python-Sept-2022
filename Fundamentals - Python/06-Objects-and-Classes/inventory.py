class Inventory:
    items = []

    def __init__(self, __capacity: int):
        self.__capacity = __capacity

    def add_item(self, item: str):
        if self.__capacity > 0:
            Inventory.items.append(item)
            self.__capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(Inventory.items)

    def __repr__(self):
        separated = ", ".join(Inventory.items)
        return f"Items: {separated}.\nCapacity left: {self.__capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
