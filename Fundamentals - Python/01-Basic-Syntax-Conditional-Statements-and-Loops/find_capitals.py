something = input()
res = [item for item in range(len(something)) if something[item].isupper()]
print(str(res))


