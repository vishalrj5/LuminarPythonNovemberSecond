class parent:
    def m1(self):
        print("inside parent")

class child():
    def m2(self):
        print("inside child")

class subchild(child,parent):
    def m3(self):
        print("inside subchild")

sc=subchild()
sc.m3()
sc.m2()
sc.m1()

#instance variables
#static variables
#different types of method
#constructor
#inhertance(1,2,3)