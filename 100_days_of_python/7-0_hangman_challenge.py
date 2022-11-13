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

# ******* using while testing code // comment out print later******
print(hidden_word) 


# replacing hidden_word letters with blanks
# display = ["_"] * len(hidden_word)
# print(display)

## Other ways to implement replacing letters with "_"
# display = []
# for letter in hidden_word:
#     display += "_"
# print(display)

display = []
word_length = len(hidden_word)

for _ in range(word_length):
    display += "_"
print(display)



# prompting user to guess a letter
user_guess = input("Guess a letter: \n").lower()

# verifing user letter input to hidden_word
for position in range(word_length):

    letter = hidden_word[position] # letter == the index positions value, letter in this case
    if letter == user_guess:
        display[position] = letter
print(f"Matches thus far: {display}")

# TODO 3a: If users letter guess matches replace blank space with letter








# # TODO 1: Create random generator from word_bank
# hidden_word = random.choice(word_bank).lower()
# print(hidden_word)

# # TODO 2: Prompt user to guess a letter 
# user_guess = input("Guess a letter: \n").lower()
    

# # TODO 3: Verify user input
# for letter in hidden_word:
    
#     if user_guess in hidden_word:
#         print(f"Matched letter: {user_guess}")
#     else:
#         print(f"{user_guess} is not a match")


