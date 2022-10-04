"""
Rock Paper Scissors

Instructions: Make a rock, paper, scissors game.

Start the game by asking the player: 
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out: 
    How you will store the user's input.
    How you will generate a random choice for the computer.
    How you will compare the user's and the computer's choice to determine the winner (or a draw).
    And also how you will give feedback to the player.
    You can find the "official" rules of the game on the World Rock Paper Scissors Association website.


"""
import time
import random


print("Welcome to the virtualized game of Paper, Rock, Scissor!")
time.sleep(1)
print("In this game you'll compete against the computer.")
time.sleep(2)


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selection = [ rock, paper, scissors ]

play_again = "yes"       

while play_again == "yes":

    player_one = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if player_one < 0 or player_one > 2:
        print("Invalid entry, exiting program")
        exit()
    
    print(f"Your selection: {selection[player_one]}\n")

    computer = random.randint(0,2)
    print(f"Computer selection: {selection[computer]}\n")

    time.sleep(1)

    win = ["Draw!\n", "WHOA, You won!!\n", "Whomp Whomp Whomp, you lost!\n"]
    print(win[player_one - computer])

    time.sleep(1)
    play_again = input("Would you like to play again? Type yes or no: \n")
    
print("Until next time!")