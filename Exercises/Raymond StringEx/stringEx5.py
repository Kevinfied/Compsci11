string = input("enter string: ")
size = int(input("enter field size: "))
length = len(string)
dotsLeft = (size - length) // 2
print("."*dotsLeft, string, "."*(size-dotsLeft-length),sep="")
