# The 3 random functions sir wants us to care about
# randint
# choice
# shuffle

# import random
from random import *       # import from the module "random' everything (*)
die = randint(1,6)      # from 1-6 inclusive
print(die)

nums = [12,4,6,77]
print(choice(nums))    # randomly picks one of the numbers
# print(nums[randint(0,len(nums)-1)]))
shuffle(nums)
print(nums)

animals = ["cat","dog","rat","bat","bee","elk"]
for i in range(5):  # can repeat
    print(choice(animals))

print("----------")

shuffle(animals)
for i in range(3):     # will not repeat
    print(animals[i])

print("-------------")

for a in animals[:3]:
    print(a)


print(random()*100)





