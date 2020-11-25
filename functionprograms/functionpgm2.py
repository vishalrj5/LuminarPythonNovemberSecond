#function with arg and return value

def add(num1,num2):
    res=num1+num2
    return res
data=add(100,200)
print(data)

def evenchk(num1):
    if(num1%2==0):
        return "even"
    else:
        return "odd"

#data=add(100,200)
print(evenchk(data))