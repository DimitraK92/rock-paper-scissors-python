import random
from options_asci import rock, paper, scissors

_ran = random
_options = [rock, paper, scissors]

def play_game():
    random_num = _ran.randint(0,2)
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if not user_input in ["0","1","2"]: print("Wrong input provided.")
    else: handle_result(_options[int(user_input)], _options[random_num])
    return input("Do you want to play again? Y/N\n").upper()

def handle_result(user_option, computer_option):
    print(user_option)
    print("Computer chose:\n" + computer_option)
    if user_option == computer_option: print("It's a draw!")
    elif user_wins(user_option, computer_option): print("You win!")
    else: print("You lose")

def user_wins(user_option,computer_option):
    if user_option == rock: 
        return computer_option == scissors
    elif user_option == paper:
        return computer_option == rock
    elif user_option == scissors:
        return computer_option == paper