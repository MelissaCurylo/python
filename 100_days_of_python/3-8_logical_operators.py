#===================================================================
#===================================================================

# Multiple logical operators in same line of code:
    # if conditional1 and conditional2 and conditional3
        # do this
    # else: 
        # do this

# Mutliple If statements in succession:
    # if condition:
        # if condititon
            # if condition

# Conditionals if / elif / else:
    # if conditional1:
        # do A
    # elif conditional2:
        # do B
    # else:
        # do this

#  if/else basic statement:
    # if condition:
        # do this
    # else:
        # do this

#===================================================================
#===================================================================

# height limit:
# must be greater than or equal to 120 cm to ride

# price points per age:
# < 12 = $5
# 12-18 = $7
# >18 = $12
# 45-50 = mid-life crisis = free ride
# wants photo= $3


# add # 45-50 = mid-life crisis = free ride

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# age = int(input("What is your age? ")) // age has to be moved in if block as it should be a local not global variable
# conditional 
bill = 0

if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.00.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.00.")
    elif age > 18 and age < 45:
        bill = 12
        print("Adult tickts are $12.00.")
    elif age >= 45 and age < 55:
        bill = 0
        print("Have a free ride on the us!")
    else:
        bill = 12
        print("Adult tickts are $12.00.")

    select_photo_choice = input("Would you like your photo taken on the ride? Type Y for Yes or N for No: ")
    if select_photo_choice.lower() == "y":
        add_photo = 3
        bill += add_photo
        print(f"You owe ${bill}")
    elif bill <= 0:
        print(f"Nothing due today, enjoy the ride!")

else:
    print("You'll need to come back when you've grown to the appropriate height to ride.")