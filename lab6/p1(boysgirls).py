i=["khushi","ayushi", ("hitarth","krutarth"), "krishna",("jay",),("khush",)]
girls=0
boys=0
for num in i :
    if isinstance(num,tuple):
       boys+=1 
    else:
       girls+=1
print("girls= ", girls)
print("boys=", boys)