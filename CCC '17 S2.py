
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
    


e = count//2
j = 0

for i in range(count-e):
    j = min(tides)
    low.append(j)
    tides.remove(j)
    
for i in range(e):
    j = max(tides)
    high.append(j)
    tides.remove(j)
    
for i in range(e):
    tides.append(low[-(i+1)])
    tides.append(high[-(i+1)])

if count % 2 != 0:
    tides.append(low[-1])

print(tides)





