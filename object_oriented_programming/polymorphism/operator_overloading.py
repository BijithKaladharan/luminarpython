class books:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return str(self.pages)
    def __add__(self,other):
        return books(self.pages+other.pages)
    def __sub__(self,other):
        return self.pages-other.pages

obj=books(100)
obj1=books(200)
obj3=books(300)

print(obj+obj1+obj3)
#print(obj-obj1)