class student:
    def set_student(self,roll,course,total):
        self.roll=roll
        self.course=course
        self.total=total
    def print_student(self):
        print("rollnumber=",self.roll)
        print("course=",self.course)
        print("total=",self.total)

obj=student()
obj.set_student(100,"mca",150)
obj.print_student()

obj.total+=50
print(obj.total)

obj1=student()
obj1.set_student(102,"mca",1009)
obj1.print_student()

