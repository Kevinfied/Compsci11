"""
Make a list of five of your friends and a list of five emotions or action words (e.g. “loves”, “hates”, “misses” ....)
For each friend in the list randomly choose a word and another friend in the list.
Don't worry if “Jack loves Jack”, he probably does anyways.
"""

from random import *

names = ["Raymond", "Eye sack", "Jerry", "Alan", "Savio"]
emotions = ["lovesssss", "punched", "defenestrated", "dislikes", "made fun of"]

for i in range(10):
    print(choice(names),choice(emotions),choice(names))


