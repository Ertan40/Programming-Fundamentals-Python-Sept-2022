cells = input().split("#") # ['High = 89', 'Low = 28', 'Medium = 77', 'Low = 23']
water = int(input())
effort = 0
all_cells = []
for element in cells:
    # level_of_fire = element.split('=')[0].strip()
    # value_of_cell = int(element.split('=')[1])
    cells_second = element.split("=") # ['Low ', ' 23']
    level_of_fire = cells_second[0].strip()#
    value_of_cell = int(cells_second[1]) # 23
    if water >= value_of_cell:
        if level_of_fire == "High":
            if 81 <= value_of_cell <= 125:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                all_cells.append(value_of_cell)
        elif level_of_fire == "Medium":
            if 51 <= value_of_cell <= 80:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                all_cells.append(value_of_cell)
        elif level_of_fire == "Low":
            if 1 <= value_of_cell <= 50:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                all_cells.append(value_of_cell)
print(f"Cells:")
for cell in all_cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(all_cells)}")
