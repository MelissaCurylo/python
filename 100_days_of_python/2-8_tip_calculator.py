# Instructions: 
    # If the bill was $150.00, split between 5 people, with 12% tip.
    # Each person should pay (150.00 / 5) * 1.12 = 33.6
    # Format the result to 2 decimal places = 33.60
    # Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
    
    #  Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input: Welcome to the tip calculator!
                # What was the total bill? $124.56
                # How much tip would you like to give? 10, 12, or 15? 12
                # How many people to split the bill? 7
# Example Output: Each person should pay: $19.93

# Hint 
    # How to round a number to 2 decimal places in Python
    # How to limit a float to two decimal places in Python

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill_total = float(input("What is the total bill: $"))
tip = int(input("What percentage of tip would you like to give (only enter numbers)? ")) 
people_splitting = int(input("How many people will split the bill? "))

bill_with_tip = bill_total * (1 + tip / 100)
bill_per_person = bill_with_tip / people_splitting
# final_split_amount = round(bill_per_person, 2) # using this option will work only on some cases for two decimal places
final_split_amount = "{:.2f}".format(bill_per_person) # using this format method turns the float into a string

print(f"Each person should pay ${final_split_amount}")