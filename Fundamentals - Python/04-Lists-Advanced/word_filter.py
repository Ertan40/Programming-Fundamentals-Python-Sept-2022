word_filter = [item for item in input().split() if len(item) % 2 == 0]
for i in word_filter:
    print(f"{i}")