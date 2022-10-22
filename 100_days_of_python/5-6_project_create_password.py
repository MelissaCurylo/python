# Password Generator Project
from operator import length_hint
import random
from typing import NoReturn

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
"""

#Eazy Level - Order not randomised solution:
password = ""

for random_letter in range(1, nr_letters + 1):
    password += random.choice(letters)
for random_number in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for random_symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

    password_combined = ''.join(password)

print("**************************************")
print(f"\nEazy level password result: {password_combined}\n")





# Hard Level - Order of characters randomised solution:
list_password = []

for random_letter in range(1, nr_letters + 1):
    list_password += random.choice(letters)
for random_number in range(1, nr_numbers + 1):
    list_password += random.choice(numbers)    
for random_symbol in range(1, nr_symbols + 1):
    list_password += random.choice(symbols)

random.shuffle(list_password)
password = ""

for makeRandomShuffle in list_password:
    password += makeRandomShuffle
print(f"Hard level password result: {password}\n")



print("**************************************")

# Another Solution with built-in methods:

# password = ''.join(random.choices(letters, k = nr_letters) + random.choices(numbers, k = nr_numbers) + random.choices(symbols, k = nr_symbols))

pass_letters  = ''.join(random.choices(letters, k = nr_letters))
pass_numbers  = ''.join(random.choices(numbers, k = nr_numbers))
pass_symbols  = ''.join(random.choices(symbols, k = nr_symbols))

easy_peasy = pass_letters + pass_numbers + pass_symbols
inputTotal = nr_letters + nr_numbers + nr_symbols
hard_pass = ''.join(random.sample(easy_peasy, k = inputTotal))

print(f"The eazy password #2 version for password result: {easy_peasy}\n")
print(f"The hard password #2 version for password result: {hard_pass}\n")

print("**************************************")