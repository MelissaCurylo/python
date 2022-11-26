import random
import time

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========
''', '''
    +---+
    |   |
    |
    |
    |
    |
=========
''']



# ******* using while testing code // comment out print later******
# print(f"\n-----------------------\n Hidden word: {hidden_word} \n-----------------------\n ***Comment this line ^^ after testing is complete***\n") 

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
time.sleep(1)

print(f"\n--<3----------------------------------\n  Welcome to Hangman \n The Game of Guessing Words \n-------------------------------<3-----\n  ") 
time.sleep(1)

word_bank = ["able", "agility", "abroad", "blanket", "birds", "balloon", "passage", "wanderlust", "wayfaring", "voyage", "voyaging", "trekking", "expedition", "home", "London", "flat", "engineer"]
hidden_word = random.choice(word_bank).lower()
word_length = len(hidden_word)
display = []
lives = 6


for _ in range(word_length):
    display += "_"
print(f"\n{display}")


while "_" in display and lives > 0:
    user_guess = input(f"\nGuess a letter: ").lower()

    for position, letter in enumerate(hidden_word):
        if letter == user_guess:
            display[position] = user_guess

    if user_guess not in hidden_word:
        lives -= 1
        time.sleep(1)
        print(f"{stages[lives]} \n\n Letter '{user_guess}' is not in the word.\n Lose a life: {lives}.\n\n")

    print(display)

if "_" not in display and lives > 0:
    time.sleep(1)
    print(f"\nYou Win! The word is: {hidden_word}.\n")
elif lives == 0:
    time.sleep(1)
    print(f"You lose, no lives left. \n The word was: {hidden_word}.\n")







# -------------------------------------------------------------------------------------------------------------
# Code blocks not used:

"""
**** alternate letter_guessed_valid() method ****
def letter_guessed_valid:():
    for position in range(word_length):
        letter = hidden_word[position] # letter == the index positions value, letter in this case
        if letter == user_guess:
            display[position] = letter


def letter_guessed_valid():
    for position, letter in enumerate(hidden_word):
        if letter == user_guess:
            display[position] = user_guess


def letter_guessed_invalid():
    if user_guess not in hidden_word:
        lives -= 1
    print(f"Lose a life, {user_guess} is not in the word.")


def game_lost():
    if lives < 0:
        print(f"You lose, no lives left. \n The word was: {hidden_word}.")

"""