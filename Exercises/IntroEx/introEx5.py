#3 Gets the coordinates for two points from the user and computes the distance.  Round your answer to two decimal places.note: you will need to get x1,y1,x2,y2 as 4 separate inputs.
x1 = float(input('Point 1 X-Coordinate: '))
y1 = float(input("Point 1 Y-Coordinate: "))

x2 = float(input("Point 2 X-Coordinate: "))
y2 = float(input("Point 2 Y-Coordinate: "))

DeltaX = ((x2 - x1) ** 2)
DeltaY = ((y2 - y1) ** 2)

Distance = float((DeltaX + DeltaY) ** (1/2))
print ("The Distance Between these two points is",Distance,"units.")
