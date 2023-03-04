#fname, lname = input("Enter the name:\n").split()
#print(lname, fname)

name = input("Enter name:\n")
spaceIndex = name.find(" ")
print(name[spaceIndex+1 :], ",", name[0:spaceIndex],sep='')
