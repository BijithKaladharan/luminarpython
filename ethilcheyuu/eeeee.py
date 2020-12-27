class employ:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig

    def __str__(self):
        return self.name+" "+self.id

f=open("emp","r")
lst=[]
for lines in f:
    id,name,exp,salary,desig=lines.rstrip("\n").split(",")
    ob=employ(id,name,exp,salary,desig)
    lst.append(ob)
    print(lst)

#for emp in lst:
    #print(emp)

upper=list(map(lambda x:x.name.upper(),lst))
print(upper)

#detail=list(filter(lambda emp:emp.desig=="developer",lst))
#for e in detail:
    #print(e)


