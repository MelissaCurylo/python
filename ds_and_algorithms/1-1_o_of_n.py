"""
Big O: O(n)
    # O(n) is always proportional and a straight line


# Example of O(n) 
    # It requires n operations to complete the process.
    # n is passed into the function and ran n times/operations.
"""
# def print_items(n):
#     for i in range(n):
#         print(i)

# print_items(10)   




""" 
Drop constants
    # Rule to simplifying O(n): O(2n) or O(10n) is denoted as O(n) as we drop the constant.
    # The behavior of the code runs n + n operations and looks like n + n = 2n 
    # Example showing code block runs n + n times with the ouput of 20 numbers being printed:
        # Ten numbers are printed from the i for loop.
        # Ten numbers are printed from the j for loop.
"""
# def print_items(n):
#     for i in range(n):
#         print(i)

#     for j in range(n):
#         print(j)

# print_items(10)   


""" 
Big O: O(n^2)
    # Rule to simplifying: O of n to any number (ie. O(n^3) or O(n^10)) will always be simplified and denoted as O(n^2).
    # The behavior of nested for loops multiplies  n * n operations and looks like n * n = n^2.
    # Line on the graph is a much steeper line compared to O(n) meaning a lot less efficient from time complexity standpoint. 
    # Example showing nested for loop runs n * n with output from 00 to 99 which is n^2 operations. 
        # The i for loop runs a 0 then the j for loop runs a 0 repeating this until each i and j have run 10 operations.
        # To note the pattern of the j for loop shows it is dependent on the i for loop.
            # Meaning that each i loop requires j to run it's full 9 operations until the ability to move back to the i loop and run it's next number.
"""
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)

# print_items(10)  


""" 
Big O: O(n^2): Taking it one level deeper
    # The behavior of this triple nested for loop runs n * n * n = n^3.
    # This is still simplified and denoted as O(n^2).
        # Does not matter if it is n^3, n^6, or n^12 as it will always be simplified as n^2.
    
"""

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j, k)

print_items(10)   