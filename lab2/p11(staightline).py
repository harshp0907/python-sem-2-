x1=int(input("enter x1 of first point= "))
y1=int(input("enter y1 of first point= "))
x2=int(input("enter x2 of seconde point= "))
y2=int(input("enter y2 of seconde point= "))
x3=int(input("enter x3 of third point= "))
y3=int(input("enter y3 of third point= "))

slope1=(y2-y1)/(x2-x1)
slope2=(y3-y2)/(x3-x2)

if(slope1==slope2):
    print("all three points are in straight line")
else:
    print("all three points are not in straight line ")    


