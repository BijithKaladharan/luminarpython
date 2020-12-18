class myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        elif a!=None:
            s=a
        return s

obj=myclass()
print(obj.sum(2,5))
print(obj.sum(6))
print(obj.sum(1,4,8))