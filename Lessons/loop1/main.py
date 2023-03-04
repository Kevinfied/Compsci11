# x = 0
# while x < 20:
#     x = x + 1
#     print(x)


# "example 2"
# name = ""
# while name != "end":     # "end" is called a sentinel - value that tells us out input is done.
#     name = input("Enter name: ")
#     print("Hello", name)

#
# name = ""
# while True:
#     name = input("Enter name: ")
#     if name == "end":
#         break       # exists the loop that it is inside.
#     print("Hello", name)


# e.g. Write a program that gets marks until -1 is entered,
#      then displays the average.

# total = 0        # accumulator - start at 0, add what you are accumulating
# num = 0          # counter - start at 0, add 1 every time your condition occurs
# while True:
#     mark = float(input("Enter mark> "))
#     if mark == -1:
#         break
#     num += 1     # num = num + 1
#     total += mark
#
# avg = total / num
# print(avg)


# Example 5 - add up all integers from 1 to 100 inclusive
#
# num = 0
# total = 0
# while num < 100:
#     num += 1
#     total += num
#
# print(total)


# # Example 6 - The for loop
# total = 0
# for day in range(1,101):
#     total += day
# print(total)



# Example 7 - exponential growth and decay
# i invest $5000 at 5% annual interest for 10 years.

# money = 5000
# for i in range(10):
#     money = money * 1.05
#
# print(money)

# Example 8 - Other versions of the for loop:
for i in range(5):  # drop the start, it starts at 0
    print(i)
for i in range(0, 21 , 2):  # Third value counts by that number
    print(i)
for i in range(20, 0, -1):
    print("*", i)

name = "Vincent Massey"
for letter in name:    # letter BECOMES each character in nam , one at a time
    if letter not in "aeiouAEIOU":
        print(letter, end="")



