import signal
from os import system
import helper

def handler(signum, frame):
    system('cls')
    exit(1)

signal.signal(signal.SIGINT, handler)

def start_game():
    system('cls')
    print('Welcome to Rock Paper Scissors game!')
    count = 1    
    play_again = True
    while (play_again):
        if count > 1: system('cls')
        play_again = helper.play_game() == "Y"
        count +=1
    system('cls')

start_game()