'''a=int(input("enter num 1 "))
b=int(input("enter num 2 "))
if a>b:
    print("a is bigger")
else:
        print("b is bigger")'''



'''a=int(input("enter num a "))
b=int(input("enter num b "))
c=int(input("enter num c "))
if a>b and a>c:
    print(a,"a is big")
elif b>a and b>c:
    print(b,"b is big")
else:
    print(c,"c is big")



a=int(input("enter num a "))
if a%2==0:
    print("even")
else:
    print("odd")



a=int(input("enter num a "))
if a%10==0:
    print("yes")
else:
    print("no")



a=int(input("enter age "))
if a<18:
    print("minor")
accept year value else:
    print("major")




a=input("enter the digits")
b=len(a)
print("number of digits",b)



year = input("Enter a year: ")

if year.isdigit():
    year = int(year)  

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Please enter a valid integer year.")





number = input("Enter a number: ")

try:
    number = float(number) 
    if number < 0:
        absolute_value = -number  
    else:
        absolute_value = number  
    print(f"The absolute value of {number} is {absolute_value}.")
except ValueError:
    print("Please enter a valid number.")'''



























































