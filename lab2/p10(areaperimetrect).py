a=int(input("enter the lenght="))
b=int(input("enter the breadth= "))
area=a*b
perimeter=2*(a+b)

if(area>perimeter):
    print("Area of rectangle is greater than it's perimeter") 
else:
    print("Perimeter of rectangle is greater than it's area")    