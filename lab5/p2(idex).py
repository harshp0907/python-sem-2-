import random
a=[]
for i in range(0,21):
    a.append(random.randint(1,100))
print(a) 
n=int(input("enter an element= "))

for i in range(21):
    if(a[i]==n):
        print(i)