countries = input().split(", ")
cities = input().split(", ")

my_dictionary = dict(zip(countries, cities))
for country, capital in my_dictionary.items():
    print(f"{country} -> {capital}")