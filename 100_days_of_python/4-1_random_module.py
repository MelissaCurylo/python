# https://en.wikipedia.org/wiki/Mersenne_Twister
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random
import pi_module


# pulling from pi_module.py
    # Use method of modules to separate large processes for readability and functionality
print(pi_module.pi)  


# random whole number
random_integer = random.randint(1, 10)
print(random_integer)


# Random float number
random_float = random.random()
print(random_float)


# Expanding float to being larger than 0.0000 through 0.9999
random_float = random.random() * 5
print(random_float)

# Setting a variable to random
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")