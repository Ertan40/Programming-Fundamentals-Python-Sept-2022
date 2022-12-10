words = input().split(" ") # ['Java', 'C#', 'PHP', 'PHP', 'JAVA', 'C', 'java']
my_dict = {}
# lower_words = [word.lower() for word in words] # ['java', 'c#', 'php', 'php', 'java', 'c', 'java']
for word in words:
    lower_word = word.lower()
    if lower_word not in my_dict:
         my_dict[lower_word] = 0
    my_dict[lower_word] += 1 # {'java': 3, 'c#': 1, 'php': 2, 'c': 1}
for key, value in my_dict.items():
    if value % 2 != 0:
        print(f"{key}", end=" ")



