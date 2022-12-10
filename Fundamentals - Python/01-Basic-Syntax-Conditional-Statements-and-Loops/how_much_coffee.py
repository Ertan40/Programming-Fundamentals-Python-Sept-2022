command = input()
events_lower = ["coding", "dog", "cat", "movie"]
events_upper = ["CODING", "DOG", "CAT", "MOVIE"]
lowercase_counter = 0
uppercase_counter = 0
total = 0

while command != "END":
    current_event = command
    if current_event in events_lower:
        lowercase_counter += 1
    elif current_event in events_upper:
        uppercase_counter += 2
    total = lowercase_counter + uppercase_counter
    if total == 5:
        print("You need extra sleep")
        break
    command = input()
# total = lowercase_counter + uppercase_counter
if not command != "END":
    print(total)




