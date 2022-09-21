# Heads or Tails

# Instructions: You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
    # Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
    # Generate a random number, either 0 or 1. Then use that number to print out Heads or Tails. 
        # e.g. 1 means Heads 0 means Tails
        # Example Output: Heads   or   Tails


#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲


import random
import time


input("Would you like to play the Heads or Tails? Type yes or no: ").lower()
play_game = "yes"
time.sleep(1)

while play_game == "yes":
    players_pick = input("Pick your coin side, type either heads or tails: ").lower()
    time.sleep(1)

    coin_toss = random.randint(0, 1)

    if coin_toss == 1:
        print("Coin toss landed on Heads")
        if players_pick.lower() == "heads":
            print("You guessed well!")
        else:
            print("Better luck next toss...")
    elif coin_toss == 0:
        print("Coin toss landed on tails")
        if players_pick == "tails":
            print("You guessed well!")
        else:
            print("Better luck next toss!")
    play_game = input("Would you like to play again? Type yes or no: ").lower()
print("Until next time!")

