class parent:
    def m1(self):
        print("inside parent")

class child(parent):
    def m2(self):
        print("inside child")

class subchild(child):
    def m3(self):
        print("inside subchild")

sc=subchild()
sc.m3()
sc.m2()
sc.m1()

ch=child()
#ch.m3() error
ch.m2()
ch.m1()

pt=parent()
pt.m1