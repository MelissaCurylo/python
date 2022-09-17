# # Pizza Order App

# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

        # Small Pizza: $15
        # Medium Pizza: $20
        # Large Pizza: $25

        # Pepperoni for Small Pizza: +$2
        # Pepperoni for Medium or Large Pizza: +$3
        # Extra cheese for any size pizza: + $1

# Example Input
    # size = "L"
    # add_pepperoni = "Y"
    # extra_cheese = "N"

# Example Output
    # Your final bill is: $28.

# Hint: 
# Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small = 15
medium = 20
large = 25
xtra_chz = 1
pep_small = 2 
pep_medium_large = 3
bill = 0

if size.lower() == "s":
    bill += small  
elif size.lower() == "m":
    bill += medium
else: 
    bill += large

if add_pepperoni.lower() == "y":
        if bill == small:
            bill += pep_small
        else:
            bill += pep_medium_large

if extra_cheese.lower() == "y":
        bill += xtra_chz
        
print(f"Your total bill comes to ${bill}.")