#prime numbers within a range

lowlimit=int(input("Enter the lower limit"))
upplimit=int(input("Enter the upper limit"))
flag=0
while(lowlimit<=upplimit+1):
    for j in range(2,lowlimit):
        if(lowlimit%j==0):
            flag+=1
            break
    if(flag==0):
        print(lowlimit)
    lowlimit=lowlimit+1
    flag=0

        #for j in range(2,i):


