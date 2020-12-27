class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name+" "+self.salary

f=open("emp","r")
lst=[]
for lines in f:
    id,name,exp,salary,desig=lines.rstrip("\n").split(",")
    #print(id,name,exp,salary,desig)

    ob=employee(id, name, exp, salary, desig)
    lst.append(ob)

for emp in lst:
    print(emp)

print("................")

#upper=list(map(lambda emp:emp.name.upper(),lst))
#print(upper)

det=list(filter(lambda emp:emp.desig=="developer",lst))
for s in det:
    print(s)
print(".......................")

sal=list(filter(lambda emp:int(emp.salary)>23000,lst))
for d in sal:
    print(d)
print(".....................")
a=list(filter(lambda emp:emp.name[0]=="a",lst))
for e in a:
    print(e)




