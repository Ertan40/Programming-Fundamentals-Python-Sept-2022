import random
from termcolor import colored
player_win_counter = 0
computer_win_counter = 0
draw_counter = 0
while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    player_move = input("Please, choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Please try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f"The computer choose {computer_move}.")
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(colored("You win!", 'green'))
        player_win_counter += 1
    elif player_move == computer_move:
        print(colored("Draw!", 'magenta'))
        draw_counter += 1
    else:
        print(colored("You lost!", 'red'))
        computer_win_counter += 1
    print(f"Your score: {player_win_counter}, computer's score: {computer_win_counter}, draw: {draw_counter}")
    play_again = input("Would you like to play again? Please type [yes] to Play Again or [no] to quit: ")
    if play_again.lower() == "no":
        if player_win_counter > computer_win_counter:
            print(colored("You won the game! Well done!", 'green'))
        elif player_win_counter == computer_win_counter:
            print(colored('Game is draw!', 'magenta'))
        else:
            print(colored("You lost the game! Please try again!", 'red'))
        print(colored("Thank you for playing!", 'blue'))
        break