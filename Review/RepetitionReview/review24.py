"""Write a program that gets a number from the user and displays all factors of that number."""

number = int(input("GIMME A NUMBER> "))

for i in range(1, number+1):
    if number % i == 0:
        print(i)
