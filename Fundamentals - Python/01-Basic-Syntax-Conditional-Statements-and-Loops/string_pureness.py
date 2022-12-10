command = input()

while command != "End":
    current_word = command
    final = ""

    for char in current_word:
        final += char*2
    if current_word == "SoftUni":
        command = input()
        continue

    print(final)
    command = input()



# def time_3(letter):
#     a = []
#     for i in range(0,len(letter)):
#         a.append(letter[i]*3)
#     return ''.join(a)
# # call the function
# print(time_3('HELLO'))

# string = "Hello World"
# final = ""
# for char in string:
#    final += char*2
#
# print(final)
