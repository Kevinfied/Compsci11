"""
selection4.py
Kevin Xu

This is a simple program that takes inputs from the value (age, number of years the user has lived at their current address, income, and the number
of years that the user has worked at their current job) and tells them what type of card that they are eligible for or if they are even eligible for one
at all.
"""


point = 0      # This is the counter for the amount of points

age = int(input("What is your age? > "))                                                         # This asks the user for their age and stores it as an integer value in variable "age"
address = float(input("How many years have you been living at your current address? > "))        # This takes the number of years that the user entered and stores it as variable "address"
income = float(input("What is your annual income? (without the money sign) > "))                 # This takes the annual income of the user and stores it as variable "income"
job = float(input("How many years have you been working at your current job? >"))                # This takes the number of years that the user has been working at their current job and stores it as variable "job"


# Checks which range that the value in "age" falls into and either gives the user points or deducts points.
if age <= 20:
    point -= 10
elif age >= 21 and age <= 30:
    point += 0
elif age >= 31 and age <= 50:
    point += 20
elif age > 50:
    point += 25

# Same thing as the lines that checks "age" but these lines checks "address" instead
if address < 1:
    point -= 5
elif address >= 1 and address <= 3:
    point += 5
elif address >= 4 and address <= 8:
    point += 12
elif address > 8:
    point += 20

# These check "income"
if income <= 20000:
    point += 0
elif income <= 45000:
    point += 12
elif income <= 70000:
    point += 24
elif income >70000:
    point += 30

# These check "job"
if job < 2:
    point -= 4
elif job >= 2 and job <= 4:
    point += 8
elif job > 4:
    point += 15

# These lines check which range that the value in the "point" counter falls into and tells the user which card they
# are eligible (if they have less than 20 points inclusive they dont get a card at all) for with their stats.
if point <= 20:
    print("""
Unfortunately, you are not eligible for a card.""")
elif point >= 21 and point <= 35:
    print("""
You are eligible for a card with a $500 limit.""")
elif point >= 36 and point <= 60:
    print("""
You are eligible for a card with a $5000 limit.""")
elif point > 60:
    print("""
You are eligible for a card with a $10000 limit!""")
