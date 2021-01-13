#
size=int(input("Enter the size of stack"))
stk=[]
top=-1

n=1
def push(element):
    global top
    print("****PUSH****\n")
    if(top>=size-1):
        print("stack is full")
    else:
        stk.append(element)
        top=top+1
    #print("***Push******")
def pop():
    print("*****PoP****")
    global top
    if(top<0):
        print("Cannot perform this operation on an empty stack")
    else:
        stk.pop(top)
        top=top-1
        print("Updated stack is\n",stk)
def display():
    print("***Display***\n")
    print(stk)
    #print(stk[0])

while(n!=0):
    option=int(input("Enter Operation u want to perform \n1)push \n2)pop \n3)display\n"))
    if(option==1):
        element=int(input("Enter the value for stack\n"))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
    else:
        print("Invalid Option")
    n=int(input("Press any key if you  want to continue (CHARGES APPLY) \n\n\npress 0 for exit"))



#queue
#fifo
#insert
#delete
                     #r
    #que=[10][20][30][40]
    #     f

#datastructures
#