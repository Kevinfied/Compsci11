# 5.Without using the method center, get a string from the user and
# a field size then display the string centered within that field, with dots "." on either side.
# You may assume that the field size is larger than the length of the string.


fieldSize = int(input("Field Size> "))
string = input("String> ")
sLength = len(string)

# print (string.count)

e = int((fieldSize - sLength) / 2)

print("." * e,string,"." * e, sep = "")



