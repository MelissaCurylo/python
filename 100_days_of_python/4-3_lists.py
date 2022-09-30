# https://docs.python.org/3/tutorial/datastructures.html
# https://www.askpython.com/python/string/convert-string-to-list-in-python
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

"""Lists Data Structure
    # Lists are order of related data stored under one variable.  
    # Lists individual data is stored in it's own index position.
    # To pull items from a list us brackets and it's index position: states_of_america[1] = "Pennsylvania".
    # .append adds one item to the end of the list.
    # .extend adds a list to the end of the list.
"""


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# Getting data from lists
print(states_of_america)
print(states_of_america[0])
print(states_of_america[-1]) # pulls from the end of the lists
print(len(states_of_america))

# Altering lists
states_of_america[1] = "PennyVania" # changes the data in index 1
states_of_america.append("Pennsylvania") # adds Pennsylvania to the end of the list
states_of_america.extend(["Sunshine State", "City that Never Sleeps", "Virginia is for Lovers"]) # Extends the list by adding (at the end) to the original list 
print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

