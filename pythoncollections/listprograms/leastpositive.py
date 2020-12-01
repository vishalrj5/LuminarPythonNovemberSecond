lst=[-2,-1,0,1,2,3,4]#find least positive missing integer
a=1
for num in lst:
    if(num>0):
            if(num==a):
            #print("IF num=", num, "a=", a)
                a=a+1
            else:
            #print("else num=",num,"a=",a)
                print(a,"is the least missing value")
                break
print(a,"is missing")


