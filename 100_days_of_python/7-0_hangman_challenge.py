"""
1. Create a random word generator.
    1a. Create visual blanks for random word.
2. Prompt user input to guess a letter for random word.
3. Conditional: Guessed letter in word?
    3a. Yes: Replace blanks with letters. 
        3a1. Conditional: All blanks filled?
            Yes: game over.
            No: loop for user input.

    3b. No: Lose body part.
        3b1. Conditional: Does user still have lives?
            Yes: loop for user input.
            No: game over.
"""

import random

word_bank = ["able", "agility", "abroad", "blanket", "birds", "balloon", "passage", "wanderlust", "wayfaring", "voyage", "voyaging", "trekking", "expedition", "home", "London", "flat", "engineer"]

# random generator from word_bank
hidden_word = random.choice(word_bank).lower()

lives = 6

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
print(f"\n-----------------------\n Hidden word: {hidden_word} \n-----------------------\n ***Comment this line ^^ after testing is complete***\n") 

print(f"\n--<3----------------------------------\n  Welcome to Hangman \n The Game of Guessing Words \n-------------------------------<3-----\n  ") 



# def hidden_word():
display = []
word_length = len(hidden_word)


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
        print(f"{stages[lives]} \n\n Letter '{user_guess}' is not in the word.\n Lose a life: {lives}.\n\n")

    print(display)

if "_" not in display and lives > 0:
    print(f"\nYou Win! The word is: {hidden_word}.\n")
elif lives == 0:
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