"""1. Pete’s Pizza Palace is famous for great pizza at reasonable prices. Make a program that will help Pete compute the
price of the orders.
Make sure you add on 14% tax and that you display the answer to 2 decimal places. Pete’s pricing is as follows:

Small: $5 for cheese + $0.75 for each additional topping.

Medium: $7 for cheese + $1.00 for each additional topping.

Large: $10 for cheese + $1.25 for each additional topping.

Pete only has 10 toppings available, so if a employee types in more than 10 there must be some mistake. Assume that they
wanted 10. Save as practicetest11.py (10 marks)"""

print("""Welcome to Pete's Pizza Palace!
Menu:
(s) Small: $5 for cheese + $0.75 for each additional topping.

(m) Medium: $7 for cheese + $1.00 for each additional topping.

(l) Large: $10 for cheese + $1.25 for each additional topping.
""")
total = 0

size = input("How fat do you want your pizza?> ")
topping = int(input("HOW MANY TOPPINGS DO YOU WANT?> "))

if topping > 10:
    topping = 10
if size == "s":
    "smol"
    total += 5
    total += (topping * 0.75)
elif size == "m":
    total += 7
    total += (topping * 1)
elif size == "l":
    total += 10
    total += (topping * 1.25)
else:
    print("Invalid input")

total = round((total * 1.14),2)
print("YOUR TOTAL IS $",total,sep="")




