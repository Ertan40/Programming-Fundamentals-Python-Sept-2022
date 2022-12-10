numbers = [int(item) for item in input().split(", ")]
positive, negative, even, odd = [], [], [], []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)
    if num >= 0:
        positive.append(num)
    if num < 0:
        negative.append(num)
positive_as_string = [str(item) for item in positive]
negative_as_string = [str(item) for item in negative]
even_as_string = [str(item) for item in even]
odd_as_string = [str(item) for item in odd]
res_positive = ", ".join(positive_as_string)
res_negative = ", ".join(negative_as_string)
res_even = ", ".join(even_as_string)
res_odd = ", ".join(odd_as_string)
print(f"Positive: {res_positive}")
print(f"Negative: {res_negative}")
print(f"Even: {res_even}")
print(f"Odd: {res_odd}")
