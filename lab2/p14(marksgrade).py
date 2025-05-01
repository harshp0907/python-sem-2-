a=int(input("enter math marks="))
b=int(input("enter physcis marks="))
c=int(input("enter chemistry marks="))

print("total marks=",a+b+c)
print("avg of marks = ", (a+b+c)/3)

if(a<=39 or b<=39 or c<=39):
    print("fail")
else:
    print("pass")


if(a<100 and a>=80):
    print("math,grad O")
elif(a<80 and a>=70):
    print("math,grade A+") 
elif(a<70 and a>=60):
    print("math,grade A") 
elif(a<60 and a>=55):
    print("math,grade B+") 
elif(a<55 and a>=50):
    print("math,grade B") 
elif(a<50 and a>=45):
    print("math,grade C")  
elif(a<45 and a>=40):
    print("math,grad P")
else:
    print("math,grade F")    





if(b<100 and b>=80):
    print("physics,grad O")
elif(b<80 and b>=70):
    print("physics,grade A+") 
elif(b<70 and b>=60):
    print("physics,grade A") 
elif(b<60 and b>=55):
    print("physics,grade B+") 
elif(b<55 and b>=50):
    print("pysics,grade B") 
elif(b<50 and b>=45):
    print("pysics,grade C")  
elif(b<45 and b>=40):
    print("pysics,grad P")
else:
    print("pysics,grade F") 





if(c<100 and c>=80):
    print("chem,grad O")
elif(c<80 and c>=70):
    print("chem,grade A+") 
elif(c<70 and c>=60):
    print("chem,grade A") 
elif(c<60 and c>=55):
    print("chem,grade B+") 
elif(c<55 and c>=50):
    print("chem,grade B") 
elif(c<50 and c>=45):
    print("chem,grade C")  
elif(c<45 and c>=40):
    print("chem,grad P")
else:
    print("chem,grade F") 