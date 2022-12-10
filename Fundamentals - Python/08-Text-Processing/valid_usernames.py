usernames = input().split(", ") #['sh', 'too_long_username', '!lleg@l ch@rs', 'jeffbutt']
valid = []
for username in usernames:
    if 3 <= len(username) <= 16:
        if username.isalnum():
            if username == username.strip():
                valid.append(username)
        if "-" in username:
            valid.append(username)

        if "_" in username:
            valid.append(username)
for v in valid:
    print(v)



