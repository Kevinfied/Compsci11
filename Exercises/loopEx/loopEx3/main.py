"""Write a program to be used by student council in this upcoming election to tabulate the votes after the election.
Your program will list, and number, the three candidates for president then allow the user to enter all of the ballets until they enter 0
then tell them who won the election and what percentage each candidate earned.
"""

print(""" The candidates are:
1. Joe Mama
2. X Æ A-Xii
3. 🤠
""")

joe = 0
X = 0
cowboy = 0

while True:
    vote = int(input("Enter your vote (0 to exit)> "))
    if vote == 0:
        break
    if vote == 1:
        joe += 1
    elif vote == 2:
        X += 1
    elif vote == 3:
        cowboy += 1

if joe > X and joe > cowboy:
    print("Joe Mama wins!")
elif X > joe and X > cowboy:
    print("X Æ A-Xii wins!")
elif cowboy > X and cowboy > joe:
    print("🤠 wins!")
else:
    print("There was a tie.")

total = joe + X + cowboy

print("Joe Mama had",round((joe/total)*100,0),"% of the votes")
print("X Æ A-Xii had",round(X/total*100),"% of the votes")
print("🤠 had",round(cowboy/total*100),"% of the votes")