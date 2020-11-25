#create a function to find factorial of a given number

def fact(num):
    fact=1
    for i in range(1,(num+1)):
        fact=fact*i
    return fact
print(fact(5))