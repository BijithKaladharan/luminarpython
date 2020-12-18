class student:

    def __init__(self,name,age,marks):
        self.name=name
        self.marks=marks
        self.age=age

    def print(self):
        print("name=",self.name)
        print("age=",self.age)
        print("marks=",self.marks)


    @classmethod
    def per_mark(cls,name,age,marks):
        return cls(name,age,(marks/100)*100)

s1=student.per_mark("ajay",18,25)
s1.print()
s2=student("maya",17,45)
s2.print()