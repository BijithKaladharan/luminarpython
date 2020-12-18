#method overriding



class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_person(self):
        print("name=",self.name,"\t","age=",self.age)

    def __str__(self):
        return "helo123"

obj=person("ajay",25)
obj.print_person()    #name= ajay 	 age= 25
print(obj.name)  #ajay

print(obj)   #__main__.person object at 0x000001B517451FD0>
              #__main__.classname object at hexadecimalvalue