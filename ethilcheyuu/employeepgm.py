from functools import*
class employee:
    def __init__(self,eid,ename,design,sal,exp):
        self.eid=eid
        self.ename=ename
        self.design=design
        self.sal=sal
        self.exp=exp
    def __str__(self):
        return self.ename+" "+self.sal

f=open("employ","r")
lst=[]
for lines in f:
    eid,ename,design,sal,exp=lines.rstrip("\n").split(",")
    obj=employee(eid,ename,design,sal,exp)
    lst.append(obj)

for emp in lst:
    print(emp)

#highest salary
sa=reduce(lambda s1,s2:s1 if s1>s2 else s2,list(map(lambda x:x.sal,lst)))
print(sa)
print("..........................")

#highest salaried employee details
detail=list(filter(lambda d:d.sal==sa,lst))
for e in detail:
    print(e)
print("..............................................")

#print highest salary corresponding to desig developer
hs=reduce(lambda sa1,sa2:sa1 if sa1>sa2 else sa2,list(map(lambda e:e.sal,list(filter(lambda c:c.design=="developer",lst)))))
print(hs)


