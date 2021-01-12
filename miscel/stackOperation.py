#
size=int(input("Enter the size of stack"))
stk=[]
top=-1

n=1
def push(element):
    global top
    if(top>=size):
        print("stack is full")
    else:
        stk.append(element)
        top=top+1
    print("***Push******")
def pop():
    print("*****PoP****"
          )
def display():
    print("***Display***")

while(n!=0):
    option=int(input("Enter Operation u want to perform 1)push 2)pop 3)display\n"))
    if(option==1):
        element=input()
        push()
    elif(option==2):
        pop()
    elif(option==3):
        display()
    else:
        print("Invalid Option")
    n=int(input("Enter do u want to continu press 0 for exit"))
