class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_person(self):
        print("name=",self.name,"\t","age=",self.age)

    def __str__(self):
        return str(self.age)


obj=person("ajay vijay",23)
obj.print_person()
print(obj)