#create a function print_employee_data()
#if we pass id as argument that function will print employee name
#if we pass id and property = designation it will print employee name and designation of that employee

f=open("employee","r")
employee={}
for lines in f:
    id,name,desig,exp,sal=lines.rstrip("\n").split(",")
    print(id,name,desig,exp,sal)
    employee[id]={"id":id,"name":name,"desig":desig,"exp":exp,"sal":sal}
#print(employee)

#f=open("employee","r")
#print_employee_data(id=1000,name="ajay",desig="developer",exp=2,sal=25000)
def print_employee_data(**kwargs):
   iden=int(input("Enter the id between 1000 and 1003\n"))
    for k,v in employee.items():
        k=int(k)
        print(k, v, iden)
        if(k==iden):
            print("k is",k,"v is",v,"iden is",iden)
            for key in v:
                if(key=='name' ):
                    print("\n",key,":",v[key])
                    break
        elif(iden>1000 or iden<1003):
            print("Value not in dictionary")
            break
print_employee_data()
