## TypeError
# What error is generated and why did this error happen?
# len(4837)
    # What => TypeError: object of type 'into' has no len()
    # Why => len() function does not like working with integers 
            # The foundation of len() function operates on strings


## TypeError
# What error is generated and why did this error happen?
# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")
    # What => TypeError: can only concatenate str (not "int") to str
    # Why => can only concatenate strings to strings


## Type Check:
# What is a way to prevent generating TypeErrors?
num_char = len(input("What is your name?"))
print(type(num_char))
    # What => By checking the data type 
    # How => Use the type() function to obtain the type of data
    # Terminal output will give type class = integer


## Type Casting (conversion):
# What is a way to convert generating TypeErrors?
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char) # this line = casting
# print("Your name has " + new_num_char + " characters.")
    # What => casting
    # How => placing num_char inside the str() function 
        # casting (converting) from str to integer


# Testing Type Check:
a = 123
print (type(a))
    # output will be <class 'int'>

ab = str(123)
print(type(ab))
    # output will be <class 'str'>

abc = float(123)
print(type(abc))
    # output will be <class 'float'>


# What will this line of code print?
print(70 + float("100.5"))
    # output => 170.5
    # Why => 70 = integer and float() function is converting the str to float


    # What will this line of code print?
print(str(70) + str(100))
    # output => 70100
    # Why => casting integer 70 into str and casting integer 100 into str then concatenating



    # Summarizing 
        # Use type() to investigate data type
        # Use data types to convert into others