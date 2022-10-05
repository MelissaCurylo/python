"""
Comparing different terms with time complexity.

"""


"""
# Time complexity = O(n)
"""
def print_items(n):
    for i in range(n):
        print(i)


#==========================================================


""" Comparison Analysis:   O(n)   VS   O(a + b) """

"""
# Time complexity = O(2n) = O(n)

    # Drop constant and simplify to O(n).
"""
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


"""
# Time complexity = O(a + b)

# There are two different parameters (a,b).
    - Can't say O(n) because both a and b cannot be equal to n as they are two different parameters.
    - The best this time complexity can be:
        - for loop on parameter a = O(a).
        - for loop on parameter b = O(b).
            - Combined and furthest this can be simplified:
                O(a) + O(b) = O(a + b)
"""
def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)



#==========================================================


""" Comparison Analysis:   O(n^2)   VS   O(a * b)   """

"""
# Time complexity = O(n^2)

    # Iterating with the same input n value.
        - O(n * n)

"""
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


"""
# Time complexity = O(a * b)

# Two different parameters (a,b).
    # The best this time complexity can be:
        - for loop on parameter a = O(a)
        - for loop on parameter b = O(b)
            - Combined and furthest this can be simplified:
                O(a) * O(b) = O(a * b)
"""
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i, j)