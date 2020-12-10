#inheritance?
class parent:
    def phone(self):
        print("have nokia 5310")
class child(parent):  #child inherits parents
    pass
c=child()
c.phone()