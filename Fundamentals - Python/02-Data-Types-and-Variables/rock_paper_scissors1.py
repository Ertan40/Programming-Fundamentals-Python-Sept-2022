import random
while True:
    player_move = input("Please, type rock, paper or scissors: ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_move = random.choice(possible_actions)
    print(f"You use {player_move}, computer chose {computer_move}.")

    if player_move == computer_move:
        print(f"If both players selected {player_move}. Draw!")
    elif player_move == "rock":
        if computer_move == "scissors":
            print("You won!")
        else:
            print('You lost!')
    elif player_move == "paper":
        if computer_move == "rock":
            print("You won!")
        else:
            print('You lost!')
    elif player_move == "scissors":
        if computer_move == "paper":
            print("You won!")
        else:
            print('You lost!')

    play_again = input("Would you like to play again? (y or n):")
    if play_again.lower() != "y":
        break