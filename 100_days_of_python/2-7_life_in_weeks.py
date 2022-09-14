# https://waitbutwhy.com/2014/05/life-weeks.html

# Instructions
    # Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
    # It will take your current age as the input and output a message with our time left in this format:
    # You have x days, y weeks, and z months left.
    # Where x, y and z are replaced with the actual calculated numbers.
    # Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input: 56
# Example Output: You have 12410 days, 1768 weeks, and 408 months left.
    # e.g. When you hit run, this is what should happen:

# Hint
    # There are 365 days in a year, 52 weeks in a year and 12 months in a year. 
    # Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

averageAge = 90
days = 365
weeks = 52
months = 12
years = 1

days_left = (int(averageAge) - int(age)) * int(days)
weeks_left = (int(averageAge) - int(age)) * int(weeks)
months_left = (int(averageAge) - int(age)) * int(months)
years_left = (int(averageAge) - int(age)) * int(years)

seconds = 60
minutes = 60
hours = 24

seconds_per_day = (int(hours) * int(minutes) * int(seconds))
minutes_per_day = int(hours) * int(minutes)

print(f"If you live to 90 years of age then you have {days_left} days, {weeks_left} weeks, {months_left} months, and {years_left} years...")
print(f"HOWEVER, each day is {hours} hours and you have {seconds_per_day} seconds, and {minutes_per_day} minutes. Do amazing things!")


# Alternative Solution
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"If you live to 90 years of age then you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, and {years_remaining} years...")
print(f"HOWEVER, each day is {hours} hours and you have {seconds_per_day} seconds, and {minutes_per_day} minutes. Do amazing things!")