number_of_rooms = int(input())
total_free_chairs = 0
total_chairs = 0
total_visitors = 0
needed_chairs = 0
room_counter = 0
for room in range(number_of_rooms):
    chairs_information = input().split() # ['XXXX', '4']
    chairs = len(chairs_information[0]) # 4
    visitors = int(chairs_information[1]) # 4
    room_counter += 1
    total_chairs += chairs
    total_visitors += visitors
    if visitors > chairs:
        needed_chairs = (visitors - chairs)
        print(f"{needed_chairs} more chairs needed in room {room_counter}")
total_free_chairs = total_chairs - total_visitors
if total_chairs >= total_visitors:
    print(f"Game On, {total_free_chairs } free chairs left")
