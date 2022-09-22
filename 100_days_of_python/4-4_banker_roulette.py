'''
Banker Roulette - Who's Paying The Bill?

Instructions: Write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

The string names_string are split into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

Example Input:
    Angela, Ben, Jenny, Michael, Chloe
    Note: notice that there is a space between the comma and the next name.

Example Output:
    Michael is going to buy the meal today!

Hint: You might need the help of the len() function.
https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

Remember that Lists start at index 0!
'''

'''
My Other Solution and prefered way for this game
Not checking bounds or edge cases leaves room for error 
Added in my second solution 👇
'''
import random


try_again = "yes"

while try_again == "yes":

    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(",") 

    if names_string.strip() and names != '':
        randomize_list = random.randint(0, len(names) -1)
        winner = names[randomize_list]
        print(f"{winner.capitalize()} is going to pay the bill today!")

    else:
        try_again = input("Your list was empty, would you like to try again? Enter yes or no: ")

print("Until next time!")




#---------------------------------------------------------------------------------------------------------------------------------------

'''
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",") 
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
'''
# My first solution and coded by rules of assignment 
# Adjusted provided code via split() above as if user input does not include a space after comma then the string is not separated... 
# Removed space
'''
import random
random_pick = random.randint(0, len(names) -1)
print(names[random_pick])
'''