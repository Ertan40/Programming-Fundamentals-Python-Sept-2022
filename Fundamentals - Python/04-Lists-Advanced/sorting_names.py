names = input().split(", ")
sorting_names = sorted(names, key=lambda x: (-len(x), x))
print(sorting_names)
