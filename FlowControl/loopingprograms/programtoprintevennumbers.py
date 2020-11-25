#program to print even numbers upto a range
lowlimit=int(input("Enter lower limit"))
i=0,j=0
limit=int(input("Enter the range"))
while(lowlimit<=limit):
    if(lowlimit%2==0):
        i=lowlimit+i
        print(lowlimit)
    lowlimit+=1

#read low limit and upper limit , find total sum of odd number and even numbers