a=input("enter your string =")
char=0
digit=0
for val in a:
    if val.isalpha():
        char+=1
    elif val.isdigit():
        digit+=1
print("char=",char)
print("digits =",digit)            