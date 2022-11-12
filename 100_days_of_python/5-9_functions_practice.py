"""
Practicing Pythonic functionality.
"""

"""
# abs()
    - Syntax: abs(enter_number)
    - Data Types: Integer, floating-point number, and complex number
    - Return Type: Absolute value
"""

test_number_integer = abs(-99)
test_number_float = abs(-99.199)
test_number_complex = abs(-3 - 4j)
raised_complex = abs(test_number_complex ** -2)

print(test_number_integer)
print(test_number_float)
print(test_number_complex)
print(raised_complex)


