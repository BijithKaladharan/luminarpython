class person:
    @staticmethod
    def -():
        print("blow")
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_person(self):
        print("name=",self.name)
        print("age=",self.age)
        print("gender=",self.gender)

obj=person("ajay",25,"male")
obj.print_person()
