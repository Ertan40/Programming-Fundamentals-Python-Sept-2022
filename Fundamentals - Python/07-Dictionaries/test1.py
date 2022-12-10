results = {}
submissions = {}
command = input()

while command != "exam finished":
    data = command.split("-")  # ['Peter', 'Java', '84']
    if len(data) == 3:
        username = data[0]
        language = data[1]
        points = int(data[2])
        if username not in results.keys():
            results[username] = [points]
        elif username in results.keys():
            results[username] += [points] # {'Peter': [84], 'George': [84, 70], 'Katy': [94]}
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
    elif len(data) != 3:
        username = data[0]
        language = data[1]
        if language == "banned" and username in results.keys():
            del results[username]
    command = input()
# print(results) # {'Peter': [84], 'George': [84, 70], 'Katy': [94]}
# print(submissions) # {'Java': 1, 'C#': 3}
print("Results:")
for username, points in results.items():
    print(f"{username} | {max(points)}")
print("Submissions:")
for language, total in submissions.items():
    print(f"{language} - {total}")