"""There are 3 types of errors


1. Syntax errors - An error that violates the structure of the language.
(e.g. missing brackets)
- the program will not run, you will get an error message.


2. Runtime Error - Program runs, then crashes.
This is causes by an index out of range, division by 0, using wrong type.


3. Logic Error - Does not crash, nut gives the wrong answer. Hardest to find




"""

name = "Big Bang"

sp = name.find(" ")

fst = name[:sp]

lst = name[sp:]

newname =""

mx = min(len(fst), len(lst))

for i in range(mx):

    newname = newname + fst[i] + lst[i]

    print (newname)



"""In all ranges, the beginning is inclusive, the end is exclusive. 
"""


express