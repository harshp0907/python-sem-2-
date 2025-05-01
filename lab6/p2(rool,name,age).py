studentdata=[(122,"khushi",19),(156,"badi",18),(134,"jay",26)]
rollnumber = []
name=[]
age=[]

for el in studentdata:
    rollnumber.append(el[0])
    name.append(el[1])
    age.append(el[2])

print("roll numbers= " , rollnumber) 
print("name= " , name) 
print("age= " , age)    