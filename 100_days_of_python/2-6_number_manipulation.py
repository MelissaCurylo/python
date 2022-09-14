
print(8 / 3) # ouput is non-manipulated
print(int(8 / 3)) # output is just the integer
print(round(8 / 3)) # rounds into a whole number
print(round(8 / 3, 2)) # rounds to two decimal places
print(round(2.66666666, 2)) # testing rounding function

print(8 / 3) # output is 2.666666665
print(type(8 / 3)) # data type = <class 'float'
print(type(8 / 2)) # even with clean division data type = <class 'float'>
print(8 // 3) # floor division denoted by //
print(type(8 // 3)) # data type = <class 'int'>



# Shorthand manipulations
result = 4 / 2
result /= 2 # result be 1 because it starts at 4/2 then divides again by 2
print(result)


score = 0
score += 1 # User scores a point
print(score)

score = 0
score -= 1 # User loses a point
print(score)



# f-String
    # can use double or single quotes

score = 0
height = 1.8
isWinning = True
score += 1 # User scores a point
# print("Your score is: " + score) # results in an error TypeError: can only concatenate str (not "int") to str
print("Your score is: " + str(score)) # long way to code this -- f-string shortens it
print(f"Your score is: {score}")  # Same result shorter code with f-string concatenation
print(f"Your score is: {score}, your height is {height}, you are winning {isWinning}")  # Adding more variables



# What is the data type of the result of variable a below?
a = int("5") / int(2.7)
print(a) # will print a float data type because it is division