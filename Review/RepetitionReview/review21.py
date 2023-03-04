"""
Write a program that gets numbers from the user until they enter zero then tells the user the
average of all the numbers, the largest number entered, the smallest number entered and the
number of negative numbers.
"""

number = 0
pool = 0
counter = 0
average = 0
largest = 0
smallest = 0
negatives = 0

while True:
    number = int(input("Gimme a number> "))
    if number == 0:
        break
    counter += 1
    pool += number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    if number < 0:
        negatives += 1

average = pool/counter
print("The average of your list of numbers is",average)
print("The largest number of your list is",largest)
print("The smallest number of your list is",smallest)
print("There was a total of",negatives,"negative numbers in your list.")

