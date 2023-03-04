"""
selection3.py
Kevin Xu

This is a program that gives you a bus ticket price depending on your age category and the type of ticket that you want to buy (1 ticket, 10 tickets, or
the monthly pass)

"""



#This is just here for my own reference
"""

Adult      $2.35      $20.30       $75
Senior     $1.60      $15.60       $38.50
Student    $1.60      $15.60       $52

"""


# Prints a chart of the value that the user should enter depending on the option that they want to pick. (A, B, or C)
print ("""
|     Age     |   Purchase Type    |  
|-------------|--------------------|
| Adult   (A) |  1 Ticket     (A)  |
| Senior  (B) |  10 Ticket    (B)  |
| Student (C) |  Tranzip Pass (C)  |
""")


age = input("What is your age group? (please enter A, B, or C) > ")      # This asks the user what their age category is and stores their input as a variable.
age = age.upper()              # This makes it so that capitalization doesn't matter. This is here because maybe users have a preference of typing either "a" or "A", but with this line,
                                # it turns "a" into "A" and "A" just would not change.


# This is just here so that if the user didnt enter either A, B, or C, it tells them that whatever they entered is not a valid input and that they have to enter A, B, or C
if age != "A" and age != "B" and age != "C":
    print("That is not a valid input. Please enter only A, B, or C according to the options in the chart above.")
    age = input("What is your age group? (please enter A, B, or C) > ")
    age = age.upper()





type = input("What would you like to purchase? (please enter A, B, or C) > ")       # This asks the user what type of purchase they want and stores their input as a variable ("type").
type = type.upper()            # This makes it so that capitalization doesn't matter


if type != "A" and type != "B" and type != "C":
    print("That is not a valid input. Please enter only A, B, or C according to the options in the chart above.")
    type = input("What would you like to purchase? (please enter A, B, or C) > ")
    type = type.upper()


# The lines below checks the stored value for "age" and then gives the user the total price of their purchase based on the value of the variable "type" that they entered.

if age == "A":
    if type == "A":
       print("That would be $2.35")
    elif type == "B":
        print("That would be $20.30")
    elif type == "C":
        print("That would be $75.00")
elif age == "B":
    if type == "A":
        print("That would be $1.60")
    elif type == "B":
        print("That would be $15.60")
    elif type == "C":
        print("That would be $38.50")
elif age == "C":
    if type == "A":
        print("That would be $1.60")
    if type == "B":
        print("That would be $15.60")
    if type == "C":
        print("That would be $52.00")
else:
    print("No.")     # This is just here to tell the user that the program is not impressed they entered another invalid input.












# if type != "A" and type != "B" and type != "C":
#     print("Please consider reading the instructions given above and try again with a valid input. \n")
#     type = input("What would you like to purchase? (ONLY ENTER A, B, OR C) > ")
#     type = type.upper()