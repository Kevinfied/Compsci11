#3.The postage you pay to send a letter from Canada depends on where you are sending it.
# For a standard sized letter the postage rates are:
# Mailing within Canada $0.52
# Mailing to USA $0.93
# Mailing Internationally $1.55
# Create a program that asks the user where they are mailing their letter then tell them the postage cost.

place = input("Where do you want to send your mail?> ")

if "anada" in place:
    print("That will be $0.52")

elif place.upper() == "USA":
    print("That would be $0.93")

else:
    print("That will be $1.55")

#elif place.upper() == "USA":
    #print("That would be $0.93")

# elif place == "USA" or place == "usa":
#     print("That would be $0.93")

