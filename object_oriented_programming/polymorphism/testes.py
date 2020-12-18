#class parent:
    #def phone(self):
        #print("i hav")


#class child(parent):
    #def phone(self):
        #print("i too hav")

#obj=child()
#obj.phone()
#........................overriding.....super().marrage()-->to print both marriage
class parent():
    def property(self):
        print("5lakh rs,lkg")
    def marriage(self):
        print("marriagae venu")
class child(parent):
    def marriage(self):
        print("marriage renu")

ch=child()
ch.property()
ch.marriage()
