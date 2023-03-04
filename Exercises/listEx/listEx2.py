"""
Make a list of ten fruits and another list of the price each fruit.
Use these two lists to create an attractive “fruit stand” menu.
"""

from random import *

fruits = ["Apple","Watermelon","Orange","Banana","Grapes","Dragonfruit","Cherry","Peach","Blueberries","Lemon"]
price = [0.99,6.99,2.39,12.99,3.57,10.12,1.42,4.13,23144123123123.12,4.44]

"""
Related lists - When you have two or more lists that are related
at each index. e.g. price[3] is the cost of fruit[3]"""

print("Raymond's Ripe Riches")
print("----------------------")
for i in range(10):
    print(fruits[i], price[i])