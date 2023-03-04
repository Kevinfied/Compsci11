# 6.Get a string from the user and display how many capital letters are in the string.
# With what we know now this is not an easy question.
# When we learn more this will become easier, but try it for now.Save as stringEx6.py

string = input("Give me a string, yo> ")
caps = int(string.count("A"))+(string.count("B"))+(string.count("C"))+(string.count("D"))+(string.count("E"))+(string.count("F"))+(string.count("G"))+(string.count("H"))+(string.count("I"))+(string.count("J"))+(string.count("K"))+(string.count("L"))+(string.count("M"))+(string.count("N"))+(string.count("O"))+(string.count("P"))+(string.count("Q"))+(string.count("R"))+(string.count("S"))+(string.count("T"))+(string.count("U"))+(string.count("V"))+(string.count("W"))+(string.count("X"))+(string.count("Y"))+(string.count("Z"))
print(caps)

count = 0
for i in range(len(string)):
    i
