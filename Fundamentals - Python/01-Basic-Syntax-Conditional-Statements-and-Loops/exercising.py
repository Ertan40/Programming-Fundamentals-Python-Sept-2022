import random

questions = ["What is the longest river in the world?", "In which city is located the highest opera building in the world?", "Which is the first programming language?"]

answered_questions = []
right_answered_question_counter = 0
false_answered_question_counter = 0
print("Welcome to Random GAME!")
while True:
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        print(current_question)
        answered_questions.append(current_question)
    else:
        continue

    if current_question == "What is the longest river in the world?":
        print("What is the longest river in the world?")
        user_answer = str(input("please enter your answer:"))
        if user_answer == "Mississipi":
            print("your answer is correct!")
            right_answered_question_counter += 1
        else:
            print("your answer is wrong!")
            false_answered_question_counter += 1
    elif current_question == "In which city is located the highest opera building in the world?":
        print("In which city is located the highest opera building in the world?")
        user_answer = str(input("please enter your answer:"))
        if user_answer == "Valencia":
            print("your answer is correct!")
            right_answered_question_counter += 1
        else:
            print("your answer is wrong!")
            false_answered_question_counter += 1
    elif current_question == "Which is the first programming language?":
        print("Which is the first programming language?")
        user_answer = str(input("please enter your answer:"))
        if user_answer == "Pyhton":
            print("your answer is correct!")
            right_answered_question_counter += 1
        else:
            print("your answer is wrong!")
            false_answered_question_counter += 1

    if right_answered_question_counter == 3:
        print("You won the game! Great!")
        break
    elif false_answered_question_counter == 2:
        print("You lost the game! Please try again!")
        break



