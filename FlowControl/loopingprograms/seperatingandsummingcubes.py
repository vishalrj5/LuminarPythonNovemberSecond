#seperate numbers and find sum of their cubes

num=int(input("Enter the number")) #123
sum=0
while(num!=0): #123!=0 12!=0 1!=0
    res=num%10 #123%10=3 12%10=2 1%10=1
    sum=sum+(res**3) #0+(3**3)=27 27+(2**3)=35 35+(1**3)=36
    num=num//10 #123//10=12 12//10=1 1//10=0
print(sum)    #36