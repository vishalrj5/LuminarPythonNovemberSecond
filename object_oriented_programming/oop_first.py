#class
#object
#reference



class person:
    def set_person(self,name,age,gender):
        #person has name
        self.name=name
        #person has age
        self.age=age
        #person has gender
        self.gender=gender
        #duty of set person() initializing person class attributes
    def print_person(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Gender=",self.gender)

#creating object
#referencename=classname()
obj=person()#created an object
obj.set_person("Ajay",25,"Male")
obj.print_person()
obj1=person()
obj1.set_person("Vijay",27,"Male")
obj1.print_person()
print("print outside class",obj.name)

obj1.age=28
obj1.print_person()
