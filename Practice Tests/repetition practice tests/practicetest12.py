"""
The Series 1/1 + 1/2 + 1/3 + 1/4 + … is a divergent series.
Create a program that will help us examine this claim.
Your program will have the user enter the number of terms from the series and tell them the sum to three decimals.

An example of a run:

Enter the number of terms:4
Save as practicetest12.py (10 marks)

2.083
"""

term = int(input("Enter the number of terms> "))
total = 0
for i in range(1,term+1):
    total += (1/i)

print(total)


