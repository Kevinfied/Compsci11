# 4.When building and enclosure for a python the amount of area at the base of the enclosure
# should be proportionate to the length of the snake.
# The minimum needed is 1/2 square foot for each foot in length up
# to and including 6 and 3/4 square foot for each foot after that.
# e.g. 9' python needs 5.25 square feet (6 * ½ + 3 * ¾)
# a program that asks the user how long their python is and tell
# them the minimum area they need for the base of its enclosure.

length = float(input("How long is da snak? (in ft.) > "))
goodName = ((length - 6) * (3/4))

if length <= 6:
    print("The base needs to be",(length * (1/2)),"ft. squared")
else:
    print("The base needs to be",(3 + goodName),"ft. squared")




