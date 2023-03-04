# Write a program that reads in a file name from the user and tells them what kind of file it is by looking at the extension.
# Your program must be able to recognize at least 5 different file types.
# e.g. "Dogs.doc" is a Word Document

name = input("File Name> ")

dot = name.find(".")
extension = (name[dot+1:])
if extension == "exe":
    print("This is an Executable file.")
elif extension == "doc":
    print("This is a Word document.")
elif extension == "pdf":
    print("This is a file in Portable Document Format.")
elif extension == "py":
    print("This is a Python program file.")
elif extension == "png":
    print("This is a Portable Network Graphics file.")
else:
    print("I have no clue.")

# i can just use if over elif in this situation


