
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_student(self):
        print("Name = ",self.name,"\t","Age = ",self.age)
    def __str__(self):
        return self.name

st=Student("Jhon",10)
st1=Student("danie",19)
st2=Student("Jim",18)

print(st)
print(st1)
print(st2)