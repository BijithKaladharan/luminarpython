#class
#object
#reference....to perform operation  [mitv-obj,remote-referenec]

#class--#design,plan,blueprint,template    TV->[mitv]
                                          #class obj


class person:
    def set_person(self,name,age,gender):
        self.name=name #person has name     #self= keyword
        self.age=age
        self.gender=gender
        #duty of set person
    def print_person(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)

obj=person()
obj.set_person("ajay",25,"male")
obj.print_person()

obj1=person()
obj1.set_person("ramji",35,"male")
obj1.print_person()
obj.age=34

obj.print_person()

obj1.age=28

obj1.print_person()