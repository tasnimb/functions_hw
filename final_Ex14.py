import random
from datetime import datetime


def rock_paper_scissors():

    def player_rps():

        player_selection = input("Please enter 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")

        if player_selection in ["R", "r", "Rock", "rock","ROCK"]:
            your_play = 'Rock'
            print("You chose: Rock")
        elif player_selection in ["P", "p", "Paper", "paper","PAPER"]:
            your_play = 'Paper'
            print("You chose: Paper")
        elif player_selection in ["S","s","Scissors","scissors","SCISSORS"]:
            your_play = "Scissors"
            print("You chose: Scissors")
        else:
            print("Invalid input, please try again")
            rock_paper_scissors()

            # player_choice = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
            # your_play = player_choice.get(player1)
            # print("You chose :", your_play)

        return your_play


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

    player_fn = player_rps()
    computer_fn = computer_rps()

    def who_wins(player=player_fn, computer=computer_fn):
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

    champion = who_wins()

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

    result()

    def play_again():

        new_game = input("Would you like to play again? Enter 'Y' for Yes , 'N' for No: ")
        new_game_input = new_game
        if new_game_input in ["Y", "y", "Yes", "yes", "YES"]:
            print("Let's play again!")
            rock_paper_scissors()
        elif new_game_input in ["N", "n", "No", "no", "NO"]:
            print("Thanks for playing, goodbye")
            exit()
        else:
            print("Invalid input. Goodbye. We hope you'll play again soon.")
            exit()

    play_again()


rock_paper_scissors()
