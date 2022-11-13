"""
Creating functions
"""

# Define function
def my_function():
    print("Hello there, ")
    print("My name is Melissa")

my_function()




"""
Practicing Pythonic functionality.
"""

"""
# abs()
    - Syntax: abs(enter_number)
    - Data Types: Integer, floating-point number, and complex number
    - Return Type: Absolute value
"""

def testing_abs(num):
    test_number_integer = abs(-99) * num
    test_number_float = abs(-99.199) 
    test_number_complex = abs(-3 - 4j) 
    raised_complex = abs(test_number_complex ** -2) 
    print(test_number_integer, test_number_float, test_number_complex, raised_complex)

print(testing_abs(2))



"""
# aiter()
    - Syntax: aiter(enter_asynchronous_iterable)
    - Data Types: asynchronous iterables
    - Return Type: asynchronous iterator; returns an asynchronous iterator for asynchronous iterable.
    - Notes: 
        - import asyncio.
        - Equivalent of iter() and next().
        - Creates asynchronous compression.  
"""
import asyncio
from asyncio import sleep

# example #1
async def hello_world():
    print("--------Hello World!--------")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world()) # blocks call and returns hello_world() coroutine until complete.
loop.close()

