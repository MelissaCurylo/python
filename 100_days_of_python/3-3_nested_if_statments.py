# Conditionals if / elif / else
    # if conditional1:
        # do A
    # elif conditional2:
        # do B
    # else:
        # do this



# height limit:
# must be greater than or equal to 120 cm to ride

# price points per age:
# < 12 = $5
# 12-18 = $7
# >18 = $12

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# age = int(input("What is your age? ")) // age has to be moved in if block as it should be a local not global variable
# conditional 
if height >= 120:  # comparison operator
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.00.")
    elif age <= 18:
        print("Please pay $7.00.")
    else:
        print("Please pay $12.00.")
else:
    print("You'll need to come back when you've grown to the appropriate height to ride.")
