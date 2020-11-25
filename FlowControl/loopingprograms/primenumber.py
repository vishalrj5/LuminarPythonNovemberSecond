#prime number

num=int(input("Enter a number")) #7
flag=0
for i in range(2,num):#2-6
    if(num%i==0):#7%2==0 7%3==0 7%4 7%5 7%6
        flag+=1
        break
if(flag==0):
    print(num,"is a prime number")
else:
    print(num,"is not a prime")
print(num%2)

#read lowlimit and upplimit ,10-50 print all prime numbers between 10-50