comp_users = input()
companies = {}

while comp_users != 'End':
    comp_users = comp_users.split(' -> ')
    company = comp_users[0]
    user = comp_users[1]
    if company not in companies:
        companies[company] = [user]     # create dictioanry key if it does not exist
    else:
        for k, u in companies.items():
            if k == company and user not in u:
                companies[company].append(user)
    comp_users = input()
# print(companies) - {'SoftUni': ['AA12345', 'CC12344'], 'Lenovo': ['XX23456'], 'Movement': ['DD11111']}
companies = dict(sorted(companies.items(), key=lambda s: s[0]))

# print(companies) - {'Lenovo': ['XX23456'], 'Movement': ['DD11111'], 'SoftUni': ['AA12345', 'CC12344']}
for k, v in companies.items():
    print(k)
    for c in v:
        print(f'-- {c}')