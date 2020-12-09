#create a function print_employee_data()
#if we pass id as argument that function will print employee name
#if we pass id and property = desig it will print employee name and designation of that employee

employee={}
f=open("employee","r")

for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    print(id,name,desig,exp,salary)



