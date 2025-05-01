import math

x1= float(input("Enter x of circle center: "))
y1 = float(input("Enter y of circle center: "))
radius = float(input("Enter radius of the circle: "))

x2 = float(input("Enter x-coordinate of the point: "))
y2 = float(input("Enter y-coordinate of the point: "))

distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


if distance < radius:
    print("The point is inside the circle.")
elif distance == radius:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")
    