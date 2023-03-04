#                 1111
#       01234567890123
name = "Vincent Massey"
# Slices - getting part of the string

print(name[0])
print (name[12])
print (name[1:4])
# up to and not including the 4

print (name[-1])
print (name[-13])

print (name[4:])
print (name[2: :3])
print (name[: :-1])

# String functions and methods
# Length of a string
print (len(name))            #function
print (name.upper())                #method  - have the string(.) do something
print (name)
print(name.replace("s", "x"))
print(name.replace("in", ""))

print(name.find(""))  #find will tell you where it starts
print(name.find('x'))   # if it doesnt exist it goes to -1
print(name.count("s"))
print (name.find("Ma"))    #Ma starts at 8





