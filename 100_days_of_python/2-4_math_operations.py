# Addition
7+3

# Subtraction
7-3

# Multiplication
7*2

# Division
    # division always gives a float
print(6/3)
print(type(6/3)) # checking data type = <class 'float'>


# Power
print(2 ** 2) # 2 * 2 * 2
print(4 ** 2) # 4 * 4


# More than one operation on same line of code
    # PEMDAS will take place for order of priority
    # Left to right order
        #()
        # **
        # * /
        # + -

# What will below print?
print(3 * 3 + 3 / 3 - 3)
    # (9 + 1 - 3) 
    # (10 - 3)
    # output = 7

# If desired output = 3, what should change?
print(3 * (3 + 3) / 3 - 3)
    # Add parans around 3+3
    # (3 + 3) will calculate first as it's priority now