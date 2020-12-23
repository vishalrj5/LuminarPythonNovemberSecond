class Employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name+" "+self.id

f=open("employee","r")
lst=[]
dict={}
for line in f:
    id, name, exp, salary, desig=line.rstrip("\n").split(",")
    ob=Employee(id,name,exp,salary,desig)
    lst.append(ob)
    if line not in dict:
        dict[id,name,exp,salary,desig]=id,name,exp,salary,desig

#for emp in lst:
 #   print(emp)

#print(dict[0])
#print all employee name in uppercase
ename=list(map(lambda emp:emp.name.upper(),lst))
print(ename)
#print employee details whose designation="developer"

design=list(filter(lambda emp:emp.desig=="developer",lst))
for emp in design:
    print(emp,"IS A DEVELOPER","\n")
#print employee details whose salary > 23000
sal=list(filter(lambda emp:int(emp.salary)>23000,lst))
for emp in sal:
    print("EMPLOYEE",emp.name,",","DESIGNATION =",emp.desig,"WITH A SALARY OF",emp.salary)