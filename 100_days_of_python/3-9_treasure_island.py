# ascii art from: https://ascii.co.uk/art/treasure
import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')


print("Welcome to Treasure Island.")
time.sleep(1)
print("Your mission is to find the treasure.") 
time.sleep(1)


#Write your code below this line 👇
print("The pyramids are to the left and a village to the right\n")
time.sleep(1)
direction = input("Which direction will you go first, type left or right? ").lower()
time.sleep(1)
if direction == "left":
    print("You've made it down the narrow pyramid hall full of booby traps - well done!\n")
    time.sleep(1)

    input("You've made it to a fork in the hall, which direction will you go? Type left or right ").lower()
    time.sleep(1)

    if direction == "right":
        print("There appears to be two treasure chests. One just beyond the water and another high up in a light up cavern\n")
        time.sleep(1)

        input("Which direction left through the water or right to the cavern? Type left or right").lower()
        time.sleep(1)

        if direction == "right":
            print("Good work mate! You've made it to the treasure chest!\n")
        else:
            print("Womp Womp Womp.... So close... The water way treasure chest was a trap!\n")
    else:
        print("Game Over - You've been captured by a booby trap... Await rescue and head home\n")
else:
    print("Game Over - Robin Hood stole your money and food, looks like you're heading home\n")

