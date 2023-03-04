"""
selection2.py
Kevin Xu

This is a simple program that tells you what how much it would cost you (in CAD) to buy a certain amount of a different currency. There are a total
of 5 different currencies that the user can choose from: EUR, USD, JPY, CNY, GBP.

"""


print("""
1 CAD = 0.691922 EUR
1 CAD = 0.745969 USD
1 CAD = 97.48957 JPY
1 CAD = 5.052939 CNY
1 CAD = 0.612593 GBP

""")

option = input("Which currency would you like to buy?> ")    # This takes the type of currency that the user wants to buy and stores it as a variable (option).
option = option.upper()       #This turns the user's input into all caps no matter what the user types.
amount = float(input("What will be the amount of your purchase?> "))     # this input takes the amount that the user would like to buy of the currency that they chose and stores it as a variable.


# The lines below determines which currency that the user chose to buy (option) and then takes the variable "amount" and does a conversion into CAD. It rounds to two decimal places and prints out the result.

if option == "EUR":
    print("That will cost you $",round((amount / 0.691922),2)," CAD", sep="")
if option == "USD":
    print("That will cost you $",round((amount / 0.745969), 2)," CAD", sep="")
if option == "JPY":
    print("That will cost you $",round((amount / 97.48957), 2)," CAD", sep="")
if option == "CNY":
    print("That will cost you $",round((amount / 5.052939), 2)," CAD", sep="")
if option == "GBP":
    print("That will cost you $",round((amount / 0.612593) , 2)," CAD", sep="")