"""
# For loop with Range

# Range 
    - Default behavior will step through all numbers from start to end of 
        specified range increasing by one. 
    - Changing the length of step is done by adding a third parameter.
"""
# prints numbers 1 through 9.
for number in range(1,10): 
    print(number)


# prints every 2nd number in range.
for stepsByTwo in range(1,12,2): 
    print(stepsByTwo)


# adds every digit in range 1 thru 100.
rangeTotal = 0
for accumulator in range(1,101):
    rangeTotal += accumulator
print(rangeTotal)