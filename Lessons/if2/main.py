mark = int(input("Enter your mark: "))

if mark >= 80:
    print("A")
elif mark <80 and mark >= 70:    #you dont really need the <80 because it goes in order and so if the input is really over 80, it wouldve been checked in the first line
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("F")