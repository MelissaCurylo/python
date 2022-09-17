# # Love Calculator

# 💪 This is a Difficult Challenge 💪

# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:
    # Take both people's names and check for the number of times the letters in the word TRUE occurs. 
        # Then check for the number of times the letters in the word LOVE occurs. 
        # Then combine these numbers to make a 2 digit number.
    
    # For Love Scores less than 10 or greater than 90, the message should be:
        # "Your score is **x**, you go together like coke and mentos."
    
    # For Love Scores between 40 and 50, the message should be:
        # "Your score is **y**, you are alright together."
    
    # Otherwise, the message will just be their score. e.g.:
        # "Your score is **z**."

    # e.g.
        # name1 = "Angela Yu"
        # name2 = "Jack Bauer"
            # T occurs 0 times
            # R occurs 1 time
            # U occurs 2 times
            # E occurs 2 times
            # Total = 5

            # L occurs 1 time
            # O occurs 0 times
            # V occurs 0 times
            # E occurs 2 times
            # Total = 3

            # Love Score = 53
            # Print: "Your score is 53."

# Example Input 1
    # name1 = "Brad Pitt"
    # name2 = "Jennifer Aniston"
    # Example Output 2
        # Your score is 73.

# The testing code will check for print output that is formatted like one of the lines below:
    # "Your score is 47, you are alright together."
    # "Your score is 125, you go together like coke and mentos."
    # "Your score is 54."

# Hint
    # The lower() function changes all the letters in a string to lower case.
    # https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

    # The count() function will give you the number of times a letter occurs in a string.
    # https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string


# 🚨 Don't change the code below 👇
from re import U


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
int_score = int(love_score)

# print(love_score)

if int_score < 10 or int_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int_score >= 40 or int_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")



#=============================================================================================================

# true = ['t', 'r', 'u', 'e']
# love = ['l', 'o', 'v', 'e']

# count1 = 0
# count2 = 0

# for i in name1:
#     for i in name2:
#         if str(i) in true:
#             count1 +=1
#         print(f"Total for {count1}")

# for i in name1:
#     for i in name2:
#         if str(i) in love:
#             count2 +=1
#         print(f"Total for {count2}")

# combined_count = 'count1' + 'count2'

# if combined_count < 10 or combined_count > 90:
#     print(f"Your score is {combined_count}, you go together like coke and mentos.")
# elif combined_count >= 40 or combined_count <= 50:
#     print(f"Your score is {combined_count}, you are alright together.")
# else:
#     print(f"Your score is {combined_count}.")

#=============================================================================================================


# a = name1
# b = name2
# symbol1 = 'true'
# symbol2 = 'love'
# for key in symbol1:
#     print(key, a.count(key))
#     print(key, b.count(key))
#     counted1 = 'a.count' + 'b.count'
#     print(f"The letters that matche true: {counted1}")

# for key in symbol2:
#     print(key, a.count(key))
#     print(key, b.count(key))
#     counted2 = 'a.count' + 'b.count'
#     print(f"The letters that matche love: {counted2}")

