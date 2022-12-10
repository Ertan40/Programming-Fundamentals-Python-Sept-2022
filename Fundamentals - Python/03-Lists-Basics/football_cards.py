cards = input().split()
list_cards = list(cards)
current_team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
current_team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
team_a = []
team_b = []
for i in range(len(list_cards)):
    element = list_cards[i]
    if element in current_team_a:
        team_a.append(element)
    elif element in current_team_b:
        team_b.append(element)
    if 11 - len(team_a) < 7 or 11 - len(team_a) < 7:
        print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}\nGame was terminated")
        break
else:
    print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}")

