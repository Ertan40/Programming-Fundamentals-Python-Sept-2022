number_of_pieces = int(input())
pianist_collection = {}
for information in range(number_of_pieces):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    pianist_collection[piece] = [composer, key] # {'Fur Elise': ['Beethoven', 'A Minor'],
    # 'Moonlight Sonata': ['Beethoven', 'C# Minor'], 'Clair de Lune': ['Debussy', 'C# Minor']}
command = input()
while command != "Stop":
    command = command.split("|")
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece not in pianist_collection:
            pianist_collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        if piece in pianist_collection:
            del pianist_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        new_key = command[2]
        if piece in pianist_collection:
            pianist_collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
result = ''
for piece in pianist_collection:
    composer = pianist_collection[piece][0]
    key = pianist_collection[piece][1]
    result += f"{piece} -> Composer: {composer}, Key: {key}\n"
print(result)

# for piece, composer_key in pianist_collection.items():
#     print(f"{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}")