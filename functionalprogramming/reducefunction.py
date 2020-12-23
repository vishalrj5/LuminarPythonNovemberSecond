from functools import *

#reduce

lst=[10,1,11,12,13,14,15,2,16,17,18]

#sum
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum,"is the sum of list",lst)

#min
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min,"is the minimum on",lst)
#max
max=reduce(lambda no1,no2:no2 if no1<no2 else no1,lst)
print(max,"is the maximum on",lst)

#find minimum of even numbers from this list
#mini=reduce(lambda no1,no2:no2 if (no1<no2 and no1%2==0) else no1,lst)
mini=reduce(lambda no1,no2:no1 if no1<no2 else no2,
            list(filter(lambda no:no%2==0,lst)))
print(mini,"is the minimum of even numbers")