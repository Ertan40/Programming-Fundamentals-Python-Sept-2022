words = input().split() # ['Ivo', 'Johny', 'Tony', 'Bony', 'Mony']
command = input().split() # ['merge', '0', '3']

while command[0] != "3:1":
    action = command[0]
    if action == "merge":
        start_idx = int(command[1])
        end_idx = int(command[2])
        merged_strings = ""
        merged_list = []
        if start_idx < 0:
            start_idx = 0
        elif start_idx > len(words):
            start_idx = len(words) - 2
        if end_idx > len(words):
            end_idx = len(words) - 1
        merged_list += words[start_idx:end_idx + 1]
        for t in merged_list:
            merged_strings += t
        del words[start_idx:end_idx + 1]
        words.insert(start_idx, merged_strings)

    elif action == "divide":
        index = int(command[1])
        partitions = int(command[2])
        how_long = len(words[index])
        space_between = how_long // partitions
        string_to_change = words.pop(index)
        print(string_to_change)
        res = []
        for x in range(partitions - 1):
            res.append(string_to_change[:space_between])
            string_to_change = string_to_change[space_between:]
        res.append(string_to_change)
        print(res)
        print(string_to_change)
        for x in res[::-1]:
            words.insert(index, x)
        print(words)
    command = input().split()

print(*words)