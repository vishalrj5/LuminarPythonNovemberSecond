from functools import *
class Employee:
    def __init__(self,id,name,desig,salary,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
        self.exp=exp
    def __str__(self):
        return self.name+" is a "+self.desig+" with salary of "+self.salary

f=open("employee","r")
employees=[]
for line in f:
    id, name, desig, salary, exp=line.rstrip("\n").split(",")
    employees.append(Employee(id,name,desig,salary,exp))

#highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
               #list(map(lambda emp:emp.salary,employees)))
#print(highest)

#print highest salarid empoyee details
#employee=list(filter(lambda emp:emp.salary==highest,employees))
#for emp in employee:
#    print(emp)

#file read
#oop
#functional programming


#find highest salary whose designation = developer

#devop=list(filter(lambda des:des.desig=="developer",employees))
#for dev in devop:
 #   print(dev)
sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
           list(map(lambda emp:emp.salary,
            list(filter(lambda des:des.desig=="developer",employees))
                    )))
print(sal)
