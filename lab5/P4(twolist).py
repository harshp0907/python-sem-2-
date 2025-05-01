import random
list=[]
list1=[]
list2=[]

for ele in range(0,30):
    list.append(random.randint(-50,50))
print(list)

for ele in list:
    if(ele<0):
        list1.append(ele)
    else:
        list2.append(ele)

print(list1)
print(list2)    

