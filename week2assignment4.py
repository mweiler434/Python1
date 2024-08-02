#This is the input
x1 = float(input("Enter X1 coordinates: "))
y1 = float(input("Enter Y1 coordinates: "))
x2 = float(input("Enter X2 coordinates: "))
y2 = float(input("Enter Y2 coordinates: "))

#This is the processing
Distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#This is the output
print("The distance between the two points is : ", Distance)
