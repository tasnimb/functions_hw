#rock paper scissors game

import random

def who_wins():

    def player_rps():

        player_selection = input("Please enter 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")

        if player_selection == 'R':
            your_play = 'Rock'
            print("You chose Rock")
        elif player_selection == 'P':
            your_play = 'Paper'
            print("You chose Paper")
        else:
            your_play = 'Scissors'
            print("You chose Scissors")

        return your_play

    # player_rps()

    def choice_conv():

        computer_choice = random.randint(0, 2)

        if computer_choice == 0:
            computer_play = 'Rock'
            print("Computer chose: Rock")
        elif computer_choice == 1:
            computer_play = 'Paper'
            print("Computer chose: Paper")
        else:
            computer_play = 'Scissors'
            print("Computer chose: Scissors")

        return computer_play

    # choice_conv()

    player1 = player_rps()
    comp1 = choice_conv()

    if player1 == comp1:
        print("You draw!")
    elif (player1 == 'Rock' and comp1 == 'Scissors') | (player1 == 'Paper' and comp1== 'Rock') | (player1 == 'Scissors' and comp1 == 'Paper'):
        print("You win!")
    else:
        print("You lose")


# who_wins()


    def play_again():

        new_game = input("Would you like to play again? Enter 'Y' for Yes , 'N' for No ")
        new_game_input = new_game
        if new_game_input == 'Y':
            print("Let's play again")
            who_wins()
        else:
            print("Thanks for playing, goodbye")
            exit()

    play_again()
who_wins()





