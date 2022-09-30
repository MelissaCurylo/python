"""
Question 1:
Given the following list:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
Which line of code will give you "Apples"?

Answer 👇
"""

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits[2])
# print(fruits[-5]) # counting from end of list the numbering starts with 1 not zero



"""
Question 2:
Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
What do you think will be printed?

Answer 👇
"""
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# It will print: Strawberries, Nectarines, Apples, Grapes, Peaches, Cherries, Melons, Lemons



"""
Question 3:
Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
What will be printed?

Answer 👇
"""

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[0])  # printing dirty_dozen index 0 = the fruits list
# print(dirty_dozen[1]) # printing dirty_dozen index 1 = the vegetables list
print(dirty_dozen[1][1]) # the behavior changes when calling two index positions and pinpoints an index within zoned indices

    # The dirty_dozen has at most two index positions but in each index position there is a list of indices fill with data like I have below: 
    #         0                1           2              3           4          5         6
    #  0  [Strawberries]   [Nectarines]  [Apples]      [Grapes]     [Peaches]  [Cherries]  [pears]
    #  1  [Spinach]        [Kale]        [Tomatoes]    [Celery]     [Potatoes]


# The result output printed: Kale 