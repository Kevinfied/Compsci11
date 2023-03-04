"""
test12.py
Kevin Xu
"""

counter = 0
while True:
    name = input("""
Enter your name> """)
    if name == "end":
        break
    counter += 1
    print("Hey ",end="")
    for i in range(0,counter-1):
        print(name + " ",end="")
    print(name,"!",sep="")

