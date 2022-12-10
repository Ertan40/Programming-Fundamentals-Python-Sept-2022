number_of_pieces = int(input())
pianist_collection = {}
for information in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pianist_collection[piece] = pianist_collection.get(composer, {})
    pianist_collection[piece][composer] = pianist_collection[piece].get(composer, key)
# print(pianist_collection)  {'Fur Elise': {'Beethoven': 'A Minor'}, 'Moonlight Sonata': {'Beethoven': 'C# Minor'},
#                               'Clair de Lune': {'Debussy': 'C# Minor'}}
command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pianist_collection:
            pianist_collection[piece] = {composer:key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pianist_collection:
            del pianist_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pianist_collection:
            for current_key in pianist_collection:
                if current_key == piece:
                    for compositor in pianist_collection[current_key]:
                        pianist_collection[current_key][compositor] = new_key
                        break
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
for keys in pianist_collection:
    for composer in pianist_collection[keys]:
        print(f"{keys} -> Composer: {composer}, Key: {pianist_collection[keys][composer]}")



