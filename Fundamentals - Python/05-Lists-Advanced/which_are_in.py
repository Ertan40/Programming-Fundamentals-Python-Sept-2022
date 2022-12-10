words_one = input().split(", ")
words_two = input().split(", ")
my_list = []
for i in words_one:
    for j in words_two:
        if i in j and i not in my_list:
            my_list.append(i)
print(my_list)