#rock paper scissors game

import random

player_selection = input("Please enter 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")
player1 = player_selection

# player_choice = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
# your_play = player_choice.get(player1)
# print("You chose :", your_play)

computer_choice = random.randint(0,2)

# comp_conversion = {0 : 'Rock', 1: 'Paper', 2:'Scissors'}
# computer_play = comp_conversion.get(computer_choice)
# print("Computer chose: ", computer_play)

if player_selection == 'R':
    your_play = 'Rock'
    print("You chose Rock")
elif player_selection == 'P':
    your_play = 'Paper'
    print("You chose Paper")
else:
    your_play = 'Scissors'
    print("You chose Scissors")

if computer_choice == 0:
    computer_play = 'Rock'
    print("Computer chose Rock")
elif computer_choice == 1:
    computer_play = 'Paper'
    print("Computer chose Paper")
else:
    computer_play = 'Scissors'
    print("Computer chose: Scissors")


if your_play == computer_play:
    print("You draw!")
elif (your_play == 'Rock' and computer_play == 'Scissors') | (your_play == 'Paper' and computer_play == 'Rock') | (your_play == 'Scissors' and computer_play == 'Paper'):
    print("You win!")
else:
    print("You lose")

new_game = input("Would you like to play again? Enter 'Y' for Yes , 'N' for No ")
new_game_input = new_game
if new_game_input == 'Y':
    print("Let's play again")
else:
    print("Thanks for playing, goodbye")
    exit()



