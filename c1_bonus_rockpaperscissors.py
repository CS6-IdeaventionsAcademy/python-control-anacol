# Name
# Date
# Python Beginnings
# Rock Paper Scissors

print("ROCK PAPER SCISSORS")

import time
import random
forever = "hi"

while forever == "hi":
    player_object = input("Enter rock, paper, or scissors: ").upper()
    if player_object == "ROCK":
        break
    elif player_object == "PAPER":
        break
    elif player_object == "SCISSORS":
        break
    else:
        print("That was not a valid guess!")
comp_guess = random.randint(1,3)
if comp_guess == 1:
    comp_guess = "ROCK"
elif comp_guess == 2:
    comp_guess = "PAPER"
else:
    comp_guess = "SCISSORS"

print("ROCK")
time.sleep(1)
print("PAPER")
time.sleep(1)
print("SCISSORS")
time.sleep(1)
print("SHOOT!")
print("You guessed " + player_object + ".")
print("I guessed " + comp_guess + ".")
if comp_guess == "ROCK":
    if player_object == "PAPER":
        print("Aw, paper covers rock! You win!")
    elif player_object == "SCISSORS":
        print("Yay, rock smashes scissors! I win!")
    elif player_object == "ROCK":
        print("TIE GAME")
if comp_guess == "PAPER":
    if player_object == "PAPER":
        print("TIE GAME")
    elif player_object == "SCISSORS":
        print("Aw, scissors cuts paper! You win!")
    elif player_object == "ROCK":
        print("Yay! Paper covers rock! I win!")
if comp_guess == "SCISSORS":
    if player_object == "PAPER":
        print("Yay! Scissors cuts paper! I win!")
    elif player_object == "SCISSORS":
        print("TIE GAME")
    elif player_object == "ROCK":
        print("Aw, rock smashes scissors! You win!")
