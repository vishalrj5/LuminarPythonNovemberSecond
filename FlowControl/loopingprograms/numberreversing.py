#123 --> 321

num=int(input("enter num"))
res=0
while(num!=0):#123!=0
    digit=num%10#digit=3
    print(digit)
    res=res*10+digit
    num=num//10 #123//10=12
print(res)


#multiplication table
#123 1**3+2**3+3**3=1+8+27=36