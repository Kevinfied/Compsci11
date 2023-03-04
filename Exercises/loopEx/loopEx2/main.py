"""As you know the inventor of the game chess was quite a clever fellow.
As the story goes the inventor presented the game to the king and the king was quite pleased.
The king asked what the inventor wanted as payment.
He asked for a grain of cereal for the first square and to have each of the next 63 squares double the previous square.
As the story goes the king agrees, but was not to pleased by the final payment.
Create a program that computes how much grain the king had to pay.
Express your answer in pounds, assume there are 7000 grains to a pound"""

square = 0
grain = 0
total = 0

while square < 64:
    square += 1
    grain = (2**(square - 1))
    total = total + grain
total = total / 7000

print(total,"pounds")


print(sum([int(2**i) for i in range(64)])/7000)

