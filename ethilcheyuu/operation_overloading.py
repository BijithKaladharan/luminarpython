class books:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return books(self.pages+other.pages)

    def __str__(self):
        return str(self.pages)


obj=books(100)
obj1=books(200)
obj2=books(300)
obj3=books(400)
obj4=books(100)

print(obj+obj1+obj2+obj3+obj4)
