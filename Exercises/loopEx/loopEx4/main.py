"""You may have heard that it is impossible to fold a standard piece of paper in half more than 7 times.
If you could fold it in half an infinite amount of times it would grow very tall and very narrow.
A standard piece of paper is 0.1 mm. The moon is 238900 miles away. How many folds would it take to reach the moon?"""

fold = 0
moon = (3.8224 * (10**11))
length = 0.1

while True:
    if length > moon:
        break
    fold += 1
    length *= 2

print(fold)






#    https://widget.rave.office.net/chat?partner=GetHelp&requestid=436f6685-e87d-4de3-8529-e402177b1b8f

#   Thanks again for contacting Microsoft Microsoft  Up and Running Support and being a valued customer, Kevin. You worked with younes today. Your case number is 1049940886.
#
# If you need additional assistance, please do not hesitate to create a new ticket by visiting https://support.microsoft.com/contactus.
#
# Take care and be well.
