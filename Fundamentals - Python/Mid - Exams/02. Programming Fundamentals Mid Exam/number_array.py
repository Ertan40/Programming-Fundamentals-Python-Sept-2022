numbers = [int(i) for i in input().split(" ")]
command = input()

while command != "End":
    command = command.split(" ")
    action = command[0]
    if action == "Switch":
        index = int(command[1])
        if 0 <= index < len(numbers):
            if numbers[index] >= 0:
                num = numbers[index]
                numbers[index] = num * -1
    elif action == "Change":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(numbers):
            numbers.insert(index, value) # num = numbers[index]
            numbers.remove(index + 1)    # numbers[index] = value
    elif action == "Sum":
        which = command[1]
        negative = [n for n in numbers if n < 0]
        negative_sum = sum(negative)
        positive = [p for p in numbers if p >= 0]
        positive_sum = sum(positive)
        all = sum(numbers)
        if which == "Negative":
            print(negative_sum)
        elif which == "Positive":
            print(negative_sum)
        elif which == "All":
            print(sum(numbers))
    command = input()
    positives = [p for p in numbers if p >= 0]
print(" ".join([str(i) for i in positives]))