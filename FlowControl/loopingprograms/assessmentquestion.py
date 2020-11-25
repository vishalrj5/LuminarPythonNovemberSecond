#read a number   2
#read nminim  8
#read nmax  40

#3,4,5,6,

num=int(input("Enter the number (POWER)"))
min=int(input("Enter the minimum limit"))
max=int(input("Enter the maximum limit"))
for i in range(1,max):
    if i**num>=min and i**num<=max:
        print(i**num,"(",i,"^",num,")")