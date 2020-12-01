lst=[21,20,18,22,7,2,25]
lst.sort()
print(lst)

#[2 ,7 ,18 , 20 , 21, 22, 25]
#
low=0
upp=len(lst)-1
flg=0
element=int(input("Enter element you want to search"))
while(low<=upp):
    mid=(low+upp)//2
    #case1
    print(low,upp,mid)
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg+=1
        break
if flg==0:
    print("No element")
else:
    print("Element found")