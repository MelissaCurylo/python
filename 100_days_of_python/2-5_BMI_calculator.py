# Instructions:
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. Conver to a whole number.
# The BMI is a measure of some's weight taking into account their height. 
    # e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
    # Example Input: weight = 80 an height = 1.75
    # Example Output: 26

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):BMI = Measuring Body Mass Index
    # Body mass is divided by the square of body height
    # BMI = weight (kg) / height^2 (m^2)
        # To convert ft to m, you need to multiply your length value by 0.3048     # 1 foot = 0.3048 meters  
        # To get kilograms from pounds, divide by 2 then take off 1/10th of your answer    # 1 kilogram = 0.453592

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)


## Alternate Way
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)


# Alternate Way
weight_as_int1 = int(weight)
height_as_float1 = float(height)
bmi = weight_as_int1 / (height_as_float1 * height_as_float1)
bmi_as_int = int(bmi)
print(bmi_as_int)