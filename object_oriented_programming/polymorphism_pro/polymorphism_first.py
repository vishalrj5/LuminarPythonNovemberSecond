#polymorphism(many forms)
    #method overloading
    #method overriding
    #operator overloading

#method overloading
#same method name but different number of args



class Maths:
    def add(self):
        print("one")
    def add(self,add):
        print("two")

m=Maths()
m.add(10)
m.add(10,10)