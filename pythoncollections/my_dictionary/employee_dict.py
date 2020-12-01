employee={"eid":1000,"desig":"developer","experience":1,"company_name":"Luminar"}

#print company name

print(employee["company_name"])

#checking for salary key in there

print("salary" in employee)

#add a new key value pair salary : 3000

employee["salary"]=30000
print(employee)

#add 5000 more rs to current salary

employee["salary"]+=5000
print(employee)

for emp in employee:
    print(emp,",",employee[emp])

for k,v in employee.items():
    print((k,v))