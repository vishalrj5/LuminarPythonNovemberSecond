

#students={
#    100:{"rol":100,"name":"test","course":"bca","total":140},
#    101:{"rol":101,"name":"test1","course":"bca","total":145},
#    102:{"rol":102,"name":"test2","course":"mca","total":130},
#}

f=open("students","r")
students={}
for line in f:
    rol,name,course,total=line.rstrip("\n").split(",")
    if rol not in students:
        students[rol]={"rol":rol,"name":name,"course":course,"total":total}
    else:
        pass
print(students)
#print(students[100])
#print(students[100]["name"])

#rol=int(input("Enter rno"))
#property=input("enter property")#total

def print_student(**kwargs):
    #kwargs={id:100,property:total}
    rol=kwargs["id"]#rol=100
    print("rol is",rol)
    print(students)
    if(rol in students):
        #prop=kwargs["property"]#prop="total"
        print(students[rol]["name"])
        if "property" in kwargs:
            prop=kwargs["prop"]
            if(prop in students[rol]):
                print(students[rol][prop])
            else:
                print("invalid prperty")
    else:
        print("student doesnot exist")

id=int(input("Enter id"))
prop=input("Enter property")
print_student(id=100,prop=prop)