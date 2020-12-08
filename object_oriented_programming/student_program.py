#student class

class student():
    def set_student(self,rno,course,total):
        self.rno=rno
        self.course=course
        self.total=total
    def print_student(self):
        print("RollNumber=",self.rno)
        print("Course=",self.course)
        print("Total=",self.total)
obj=student()
obj.set_student(100,"mca",150)
obj.print_student()

obj.total+=50
obj.print_student()
