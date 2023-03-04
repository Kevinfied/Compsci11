# In Ontario we have two forms of sales tax PST & GST on fast food.
# GST is 5% and always charged on fast food,
# PST is 8% but only charged when the price of the meal is $4.00 or over.
# Create a program that gets the base price of a meal and outputs the total after tax.

basePrice = float(input("Base Price> "))
GST = basePrice * 0.05
PST = basePrice * 0.08

if basePrice < 4:
    print("That will be $", round((basePrice + GST),2), sep='')
else:
    print("That will be $", round((basePrice + GST + PST),2), sep='')