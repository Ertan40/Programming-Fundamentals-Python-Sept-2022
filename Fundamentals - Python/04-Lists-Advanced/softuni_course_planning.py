lessons = input().split(", ") # ['Data Types', 'Objects', 'Lists']
command = input().split(":") # ['Add', 'Databases']

while command[0] != "course start":
    action = command[0]
    lesson_title = command[1]
    if len(command) > 2:
        lesson_title_or_index = command[2]

    if action == "Add":
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    elif action == "Insert":
        if lesson_title not in lessons:
            lessons.insert(int(lesson_title_or_index), lesson_title)

    elif action == "Remove":
        if lesson_title in lessons:
            lessons.remove(lesson_title)
        if f"{lesson_title}-Exercise" in lessons:
            lessons.remove(f"{lesson_title}-Exercise")

    elif action == "Swap":  # ['Arrays', 'lists', 'Methods']
        if lesson_title in lessons and lesson_title_or_index in lessons:
            lesson_title_idx = lessons.index(lesson_title)
            lesson_title_or_index_idx = lessons.index(lesson_title_or_index)
            lessons[lesson_title_idx], lessons[lesson_title_or_index_idx] = \
                lessons[lesson_title_or_index_idx], lessons[lesson_title_idx]

            if lesson_title_or_index and f"{lesson_title_or_index}-Exercise" in lessons:
                index_lesson_title_or_index = lessons.index(lesson_title_or_index) + 1
                lessons.insert(index_lesson_title_or_index, f"{lesson_title_or_index}-Exercise")
                lessons.pop(lessons.index(f"{lesson_title_or_index}-Exercise", lessons.index(f"{lesson_title_or_index}-Exercise") + 1))
            if lesson_title and f"{lesson_title}-Exercise" in lessons:
                index_lesson_title = lessons.index(lesson_title) + 1
                lessons.insert(index_lesson_title, f"{lesson_title}-Exercise")
                lessons.pop(lessons.index(f"{lesson_title}-Exercise", lessons.index(f"{lesson_title}-Exercise") + 1))

    elif action == "Exercise":
        if lesson_title not in lessons:
            exercise_word = f"{lesson_title}-Exercise" # lesson_title + "-Exercise"
            lessons.append(lesson_title)
            lessons.append(exercise_word)

        elif lesson_title in lessons and f"{lesson_title}-Exercise" not in lessons:
            lessons.insert(lessons.index(lesson_title) + 1, f"{lesson_title}-Exercise")
    command = input().split(":")
for index, item in enumerate(lessons):
    print(f"{index + 1}.{item}")
