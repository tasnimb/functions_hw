import random
from datetime import datetime


def player_rps():

     player_selection = input("Please enter 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")

     if player_selection in ["R", "r", "Rock", "rock", "ROCK"]:
        player_selection = 'Rock'
        print("You chose: Rock")
     elif player_selection in ["P", "p", "Paper", "paper", "PAPER"]:
        player_selection = 'Paper'
        print("You chose: Paper")
     elif player_selection in ["S", "s", "Scissors", "scissors", "SCISSORS"]:
        player_selection = "Scissors"
        print("You chose: Scissors")
     else:
        print("Invalid input, please try again")
        player_rps()

            # player_choice = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
            # player_selection = player_choice.get(player1)
            # print("You chose :", player_selection)

     return player_selection


def computer_rps():

    computer_selection = random.randint(0, 2)

    if computer_selection == 0:
        computer_play = 'Rock'
        print("Computer chose: Rock")
    elif computer_selection == 1:
        computer_play = 'Paper'
        print("Computer chose: Paper")
    else:
        computer_play = 'Scissors'
        print("Computer chose: Scissors")

            # comp_conversion = {0 : 'Rock', 1: 'Paper', 2:'Scissors'}
            # computer_play = comp_conversion.get(computer_choice)
            # print("Computer chose: ", computer_play)

    return computer_play


def who_wins(player, computer):
    if player == computer:
        print("You draw!")
        winner = "draw"
    elif (player == 'Rock' and computer == 'Scissors') | (player == 'Paper' and computer == 'Rock') \
              | (player == 'Scissors' and computer == 'Paper'):
        print("You win!")
        winner = "player"
    else:
        print("You lose")
        winner = "computer"
    return winner


def result():
    # file_record = open("win_tally.txt", "w")
    file_record = open("win_tally.txt", "a")
    now = datetime.now()
    time_now = now.strftime("%a, %d %B, %y")

    if champion == "draw":
        file_record.writelines("It was a draw on: {}\n".format(time_now))
    elif champion == "player":
        file_record.writelines("You won against the computer on: {}\n".format(time_now))
    else:
        file_record.writelines("The computer beat you on: {}\n".format(time_now))
    file_record.close()


def play_again():

    new_game = input("Would you like to play again? Enter 'Y' for Yes , 'N' for No: ")
    new_game_input = new_game
    if new_game_input in ["Y", "y", "Yes", "yes", "YES"]:
        print("Let's play again!")
        player_rps()
    elif new_game_input in ["N", "n", "No", "no", "NO"]:
        print("Thanks for playing, goodbye")
        exit()
    else:
        print("Invalid input. Goodbye. We hope you'll play again soon.")
        exit()