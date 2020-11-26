lst=[9,8,7,6,4,3,2]#[10,9,8,7,3,2,1]
#lst=[10,11,8,4,3]#[11,12,9,3,2] num > 5 num+1 else num-1
oplst=[]
for num in lst:
    if num>5:
        a=num+1
        oplst.append(a)
    else:
        a=num-1
        oplst.append(a)
print("input list =",lst)
print("output list =",oplst)
print("List length is",len(lst))
