from datetime import date
tupel1=(25,3,2006)
tupel2=(24,2,2007)

d1=date(tupel1[2],tupel1[1],tupel1[0])
d2=date(tupel2[2],tupel2[1],tupel2[0])


difference= (abs(d2-d1).days)
print(f"num of dys betw {d1} and {d2} is {difference} days")