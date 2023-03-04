"""
test11.py
Kevin Xu
"""


points = 0

while True:
    cards = int(input("How many cards do you have?> "))
    if cards >= 1 and cards <= 7:
        points = cards
        break
    elif cards >= 8 and cards <= 10:
        points = cards * 2
        break
    elif cards >= 11 and cards <= 13:
        points = cards * 3
        break
    elif cards >= 14 and cards <= 15:
        points = cards * 4
        break
    elif cards == 16:
        points = cards * 5
        break
    else:
        print("That is not a valid input!")

print("That is",points,"points.")
