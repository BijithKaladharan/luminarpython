class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_student(self):
        print("name=",self.name,"\t","ages=",self.age)

    def __str__(self):
        return "hhh"

st=student("john",18)
st1=student("danie",19)
st2=student("ram",30)
print(st)
print(st1)
print(st2)