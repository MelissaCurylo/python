"""
Treasure Map Challenge

Instructions: 
    # You are going to write a program which will mark a spot with an X. In the starting code, you will find a variable called map.

    # This map contains a nested list. When map is printed this is what the nested list looks like:

        ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
        In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

        ['⬜️', '⬜️', '⬜️']
        ['⬜️', '⬜️', '⬜️']
        ['⬜️', '⬜️', '⬜️']
        This is to try and simulate the coordinates on a real map.


Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
    # The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
        # First your program must take the user input and convert it to a usable format.
        # Next, you need to use it to update your nested list with an "x".

    # Example Input 1
        # column 2, row 3 would be entered as: 23
    # Example Output 1
            ['⬜️', '⬜️', '⬜️']

            ['⬜️', '⬜️', '⬜️']

            ['⬜️', 'X', '⬜️']

    # Example Input 2: 
        # column 3, row 1 would be entered as: 31
    # Example Output 2
            ['⬜️', '⬜️', 'X']

            ['⬜️', '⬜️', '⬜️']

            ['⬜️', '⬜️', '⬜️']
        e.g. When you hit run, this is what should happen:

Hint:
    # Remember that Lists start at index 0!
    # Map is just a variable that contains a nested list. It's not related to the map function in Python.
"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Taking user input and converting it into integers and dedicating which number go to which index.
horizontal = int(position[0]) # horizontal must be set to index 0 // column
vertical = int(position[1]) # vertical must be set to index 1  // row

map[vertical - 1][horizontal -1] = "X" # vertical specifies the row and adding on horizontal which is the column


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")





# ==============================================================================================================================
# Another Solution:

# # Taking user input and converting it into integers and dedicating which number go to which index.
# horizontal = int(position[0]) # horizontal must be set to index 0 // column
# vertical = int(position[1]) # vertical must be set to index 1  // row

# # print(map[vertical -1]) # Test print // change the tile to an asterik to test. 

# spot_marked = map[vertical - 1] # choosing row from map where vertical variable desired place. 
# spot_marked[horizontal -1] = "X"  # replacing the row element with "X" via horizontal variable holding row number.

# ==============================================================================================================================
# Another solution:

# column = int(position[0]) -1  # vertical
# row = int(position[1]) -1 # horizontal
# map[row][column] = "X" # showing transpose of column and row to place x in correct place. 

# =============================================================================================================================
"""
Working it out:

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# map is a nested list that contains three rows:    map = [row1, row2, row3]
                                                    map[0] # pulls map row1
                                                    map[1] # pulls map row2
                                                    map[2] # pulls map row3

list 1 = row1 = [1, 2, 3]   -> index 0
list 2 = row2 = [4, 5, 6]   -> index 1
list 3 = row3 = [7, 8, 9]   -> index 2

        column 1 = [1, 4, 7]   -> index 0
        column 2 = [2, 5, 8]   -> index 1
        column 3 = [3, 6, 9]   -> index 2

    # column is the transpose of row - take the row and convert it into a column


# Place "X" at [column, row]
        column = horizontal = position[0] 
        row = vertical = position[1]

    1. Define user input for horizontal and vertical:
            horizontal = int(position[0]) 
            vertical = int(position[1])
    2. Use string splitter to change string to integer: 
            int(position[index_position])
    3. Transpose user input by assigning the vertical then rename horizontal to "X"
            spot_marked = map[vertical - 1]
            spot_marked[horizontal -1] = "X"   // spot_marked with "X"

Inserting X at position 4 would be []

# Khan Academy: Transpose of a matrix
# https://www.youtube.com/watch?v=TZrKrNVhbjI
"""