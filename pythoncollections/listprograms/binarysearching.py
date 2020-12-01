#linear search
#hackerrank
#account
lst=[1,2,3,4,5,6,7,8]

element=int(input("Enter the element"))

flag=0
for num in lst:
    if(element==num):
      flag+=1
      break
    else:
        flag=0
if flag==0:
    print("Element not found")
else:
    print("Element found")

#data structers
#1.Linear datastructures -> arrays,stack, queue
#2.Non linear datastructures
