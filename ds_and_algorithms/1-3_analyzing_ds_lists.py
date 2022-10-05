"""
Big O of Lists

# Analyzing Data Structure Lists with Time Complexity.


"""

my_list = [11, 3, 23, 7, 12, 11, "Hello", "World", "I", "LOVE"]



###=======================================================================
"""  .append()   VS    .insert() """

"""
.append()
    # Time complexity: O(1) Constant Time where n is for the number of operations.
    # Adds to the end of the list.
        - There isn't the need to re-index as the addition is at the end.
        - Only one operation needed.
"""
print(my_list.append("Python"))


"""
.insert(0)
.insert(6, "London is Calling")
    # Time complexity: O(n) Linear Time where n is for the number of items in the list. 
    # Inserting at index positions 0 and 6 requires movement.
        - Both opertaions require the need to re-index as the insertion changes the index positions.
"""
print(my_list.insert(0, "PyPy"))
print(my_list.insert(6, "London is Calling"))




###=======================================================================
"""  .pop()   VS    .pop(0) """

"""
.pop()
    # Time complexity: O(1) Constant Time where n is for my number of operations. 
    # removes from the end of the list.
        - There isn't the need to re-index as the removal is at the end.
        - Only one operation needed.
"""
print(my_list.pop())


"""
.pop(0)
    # Time complexity: O(n) Linear Time where n is the number of items in the list.
    # removes from the front of the list.
        - This requries re-indexing of the list as the removal changes the index positions.
"""
print(my_list.pop(0))