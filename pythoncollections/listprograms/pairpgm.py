lst=[1,2,3,4,6]
#6 (4,2)
# 1 2 3 4 6
# l       u
low=0
upp=len(lst)-1
element=12
while(low<upp):
    total=lst[low]+lst[upp]
    if(element<total):
        upp=upp-1
    elif(element>total):
        low=low+1
    elif(element==total):
        print("Pair is","(",lst[low],",",lst[upp],")")
        break