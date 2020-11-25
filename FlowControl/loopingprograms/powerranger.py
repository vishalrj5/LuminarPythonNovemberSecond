#2 2+22

#3 3+33+333

num=input("Enter a number") #3
i=1
total=0
while(i<=int(num)): #1<=3 2<=3
    #print(num*i) #"3"*1=3 "3"*2=33 "3"*3=333
    data=num*i #"3"*1=3 "3"*2=33 "3"*3=333
    total=total+int(data) #0+3=3 3+33=36 36+333=369
    i+=1 #2 3 4
print(total)   #369