

# Should i use a for loop, or a while loop?
# If you know how many times you re going to loop,
# before you start looping, use a for loop.
# Otherwise , use a while loop.

fails = 0

while True:
    mark = int(input("Enter mark: "))
    if mark == -1:
        break
    if mark < 50:
        fails += 1

print("You failed", fails, "classes")