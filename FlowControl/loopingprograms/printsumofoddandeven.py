#Read lower and upper limits and find sum of even and odd numbers.

low=int(input("Enter the lower limit"))
high=int(input("Enter the upper limit"))
i=0
j=0
while(low<=high):
    if(low%2==0):
        i=low+i
    elif(low%2==1):
        j=low+j
    low=low+1
print("Sum of even is",i)
print("Sum of odd is",j)
