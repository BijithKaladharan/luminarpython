class student:
    def set_student(self,name,roll,course,total):
        self.name=name
        self.roll=roll
        self.course=course
        self.total=total

    def print_student(self):
        print("name=",self.name)
        print("roll=",self.roll)
        print("course=",self.course)
        print("total=",self.total)
obj=student()
obj.set_student("vijay",1,"cs",105)
obj.print_student()

obj.roll+=100
obj.print_student()

obj1=student()
obj1.set_student("amal",24,"cs",190)
obj1.print_student()