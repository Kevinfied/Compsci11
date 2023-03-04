#4 At Jenny’s birthday party she orders a 32-piece pizza.  Have the user (probably Jenny) enter the number of people at the party that will be eating pizza and output the number of slices each one gets.  As you know the pizza might not divide evenly.  There are two ways to handle this. The first is to ignore the extra pieces and give everyone the same amount.  The second way is to cut up the extra pieces so that everyone gets the same amount.  Your program must output both options. E.g.Number ofguests: 10Option 1: 3 slices each, 2 left overOption 2: 3.2 slices eachSave as introEx6.py
NumPPL = int(input("Number of Guests: "))
Remainder = (30 % NumPPL)
RemainderSplit = (30 // NumPPL)
CompleteSplit = (30 / NumPPL)

print ("Option 1:", RemainderSplit,"slice each,",Remainder,"left over.")
print ("Option 2:", CompleteSplit,"each.")


