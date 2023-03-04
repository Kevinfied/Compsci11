"""
In order for a password to be considered valid it must be at least 6 characters long
and have at least one number in it and at least 1 character in it.
Write a program that lets the user continue to enter possible passwords until they
enter "end". For each password tell them if it is "VALID" or "INVALID".
"""

character = False
number = False

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while True:
    password = input("Password> ")
    if password == "end":
        break


    if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
        number = True
    if "q" in password or "w" in password or "e" in password or "r" in password or "t" in password or "y" in password or "u" in password or "i" in password or "o" in password or "p" in password or "a" in password or "s" in password or "d" in password or "f" in password 



    if len(password) >= 6:
        if number == True:
            if letter == True:
                print("VALID")
