"""
selection1.py
Kevin Xu

This is a program that tells you the direction you're facing based on compass bearing value that the user entered.
"""


bearing = float(input("Give me a compass bearing value> "))      # This is the compass bearing value that the user enters. It stores it as a float variable so it can be more accurate.

if bearing > 360:
    bearing -= 360    # This is so when the user gives a value over 360, it converts it to
                               # the value that it would overlap when it goes around the compass.


# The lines below just gives your bearing value a direction. If the value in the bearing variable fits fits into the range for a certain direction, then that direction is the where your bearing value would be facing.


if bearing > 315 and bearing <= 360:
    print("You are facing to the North.")
if bearing < 45 and bearing >= 0:
    print("You are facing to the North.")
if bearing == 45:
    print("You are facing exactly to the North-East.")
if bearing > 45 and bearing < 135:
    print("You are facing to the East.")
if bearing == 135:
    print("You are facing exactly to the South-East.")
if bearing > 135 and bearing < 225:
    print("You are facing to the South.")
if bearing == 225:
    print("You are facing exactly to the South-West.")
if bearing > 225 and bearing < 315:
    print("You are facing to the West.")
if bearing == 315:
    print("You are facing exactly to the North-West.")

