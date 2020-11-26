lst=[5,4,3,2]#[9,10,11,12]
#lst=[5,6,3,4] = o/p = [13,12,15,14]
oplst=[]
total=0
for num in lst:
    total=sum(lst)-num
    oplst.append(total)
print(oplst)
