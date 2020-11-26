#add a limit of numbers

limit=int(input("Enter limit"))
lst=[]
lst2=[]
for i in range(1,limit+1):
    if(i%2==0):
        lst.append(i)
    else:
        lst2.append(i)
print("odd list =",lst2)
print("even list =",lst)

#store odd and even numbers in to seperate list