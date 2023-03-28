
tides = []
count = 0
low = []
high = []
while True:
    

    tide = int(input("Measurement of the tide> "))
    if tide == 0:
        break
    tides.append(tide)
    count += 1
    

print(tides)
print(count)

e = count//2
print(f" the value of e is {e}")
j = 0

for i in range(e):
    j = min(tides)
    print(j)
    low.append(j)
    print(low)
    tides.remove(j)
    print(tides)
    


