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
