# Mutliple If statements in succession



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

# wants photo
# wants photo= $3

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
    else:
        bill = 12
        print("Adult tickts are $12.00.")

    select_photo_choice = input("Would you like your photo taken on the ride? Type Y for Yes or N for No: ")
    if select_photo_choice == "Y" or "y":
        add_photo = 3
        total_bill = add_photo + bill
        print(f"You owe ${total_bill}")
    else:
        print(f"You owe ${bill}")

else:
    print("You'll need to come back when you've grown to the appropriate height to ride.")