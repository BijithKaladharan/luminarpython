# find highest salary
from functools import*
class Employee:
    def __init__(self,eid,ename,desig,sal,exp):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.sal=sal
        self.exp=exp

    def __str__(self):
        return self.ename+" "+self.sal

#read from file
f=open("employee","r")
employees=[]
for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))
for emp in employees:
    print(emp)

print("...............................")
#highest salary

highest=reduce(lambda sa1,sa2:sa1 if sa1>sa2 else sa2,list(map(lambda emp:emp.sal,employees)))
print(highest)

#print salary employee details
employee=list(filter(lambda e:e.sal==highest,employees))
for emp in employee:
    print(emp)
print("...........................")

#print highest salary corresponding to desig developer

h=reduce(lambda s1,s2:s1 if s1>s2 else s2,list(map(lambda emp:emp.sal,
         list(filter(lambda emp:emp.desig=="developer",employees)))))
for emp in employee:
    print(emp)