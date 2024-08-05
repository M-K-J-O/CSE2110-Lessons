#rock_paper_scissors.py

"""
Title
Date
Author
"""

import random
from z_myfunc import *

SCORE = 0
OPPONENT_SCORE = 0

print("")
print("ROCK PAPER SCISSORS!")
print("")
START = input(print("Press ENTER to Start: "))
print("")

while START == "":

    print("")
    WEAPON = input("Enter a choice: \"Rock\", \"Paper\", \"Scissors\" ")
    POSSIBLE_WEAPONS = ("Rock", "Paper", "Scissors")
    OPPONENT_WEAPON = random.choice(POSSIBLE_WEAPONS)
    print("")
    print(f" You Chose {WEAPON} and your Opponent Chose {OPPONENT_WEAPON}")
    print("")

    if WEAPON == OPPONENT_WEAPON:
        print(f" {WEAPON} and {OPPONENT_WEAPON} beat each other and both get destroyed!")
        print("")
        print(" No winners!")
        print("")
        SCORE = SCORE + 0
        OPPONENT_SCORE = OPPONENT_SCORE + 0
        print(" Score + 0, Opponent Score + 0")
        print(f" Your Current Score is: {SCORE}")
        print(f" Your Opponents Score is: {OPPONENT_SCORE}")
        print("")
        askContinue()

    elif WEAPON == "Rock" and OPPONENT_WEAPON == "Scissors" or WEAPON == "Paper" and OPPONENT_WEAPON == "Rock" or WEAPON == "Scissors" and OPPONENT_WEAPON == "Paper":
        print(f" {WEAPON} Beats {OPPONENT_WEAPON} and {OPPONENT_WEAPON} gets destroyed!")
        print("")
        print(" Player Wins!")
        print("")
        SCORE = SCORE + 1
        OPPONENT_SCORE = OPPONENT_SCORE + 0
        print(" Score + 1, Opponent Score + 0")
        print(f" Your Current Score is: {SCORE}")
        print(f" Your Opponents Score is: {OPPONENT_SCORE}")
        print("")
        askContinue()

    elif OPPONENT_WEAPON == "Rock" and WEAPON == "Scissors" or OPPONENT_WEAPON == "Paper" and WEAPON == "Rock" or OPPONENT_WEAPON == "Scissors" and WEAPON == "Paper":
        print(f" {OPPONENT_WEAPON} Beats {WEAPON} and {WEAPON} gets destroyed!")
        print("")
        print(" Opponent Wins!")
        print("")
        SCORE = SCORE + 0
        OPPONENT_SCORE = OPPONENT_SCORE + 1
        print(" Score + 0, Opponent Score + 1")
        print(f" Your Current Score is: {SCORE}")
        print(f" Your Opponents Score is: {OPPONENT_SCORE}")
        print("")
        askContinue()
    else:
        print("That is not a available Weapon!")

