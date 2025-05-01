list1=[2,4,3,6,4,7]
list2=[1,6,2,5,3,2]
list3=[]
for ele in list1:
    if ele not in list2:
        list3.append(ele)

print(list3)