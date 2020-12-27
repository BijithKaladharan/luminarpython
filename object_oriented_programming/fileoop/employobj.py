class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name

f=open("employee","r")
lst=[]
for lines in f:
    id, name, exp, salary, desig=lines.rstrip("\n").split(",")
    #print(id,name,exp,salary,desig)

    ob=employee(id, name, exp, salary, desig) #oro thavana obj create cheyithu
    lst.append(ob)

for emp in lst:
    print(emp)

#print all employee name in upper case
#upper=list(map(lambda emp:emp.name.upper(),lst))
#print(upper)
#print employee details whose designation="developer"
#empdetail=list(filter(lambda emp:emp.desig=="developer",lst))
#print(empdetail)
#for emp in empdetail:
    #print(emp)

#print employee whose salary>2300

#high=list(filter(lambda emp:int(emp.salary)>23000,lst))
#for emp in high:
    #print(emp)