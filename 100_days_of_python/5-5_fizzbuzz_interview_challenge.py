"""
Challenge: FizzBuzz

Instructions: You are going to write a program that automatically prints the solution to the FizzBuzz game.
        Your program should print each number from 1 to 100 in turn. Each number/text should be printed on a separate line.
        
        When the number is divisible by 3 then instead of printing the number it should print "Fizz".
        When the number is divisible by 5, then instead of printing the number it should print "Buzz".
        And if the number is divisible by both 3 and 5 (e.g. 15) then instead of the number it should print "FizzBuzz".

        e.g. it might start off like this: 
            1
            2
            Fizz
            4
            Buzz
            Fizz
            7
            8
            Fizz
            Buzz
            11
            Fizz
            13
            14
            FizzBuzz
            .... etc.

    Hint: Remember your answer should start from 1 and go up to and including 100. 

"""

# My solution:
    # The if statement with most complexity should be first to avoid skipping steps in checking conditions. 
    # Meaning that if the number is both divisible by 3 and 5 and inside for loop if statements begin with fizzDivisibleBy or buzzDivisibleBy 
        # the loop would exit at one of these and never get to Fizz Buzz.


rangeStart = 1
rangeEnd = 101
number = 0

fizzDivisibleBy = 3
buzzDivisibleBy = 5

for number in range(rangeStart, rangeEnd):
    if number % fizzDivisibleBy == 0 and number % buzzDivisibleBy == 0: 
        print("Fizz Buzz")
    elif number % fizzDivisibleBy == 0:
        print("Fizz")
    elif number % buzzDivisibleBy == 0:
        print("Buzz")
    else:
        print(number)