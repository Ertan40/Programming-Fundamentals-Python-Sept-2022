version = [int(item) for item in input().split(".")] # ['1', '2', '3']
version[-1] += 1
if version[-1] == 10:
    version[-2] += 1
    version[-1] = 0
if version[-2] == 10:
    version[-3] += 1
    version[-2] = 0
if version[-3] == 10:
    version[-3] = 9
version_as_string = [str(item) for item in version]
print(".".join(version_as_string))
