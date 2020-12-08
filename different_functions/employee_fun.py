#create a function print_employee_data()
#if we pass id pass argument that function will print employee name
#if we pass id and property = desig it will print employee name and designation of

employee={}
f=open("employee","r")

for lines in f:
    words=lines.rstrip("\n").split(" ")
    print(words)

def print_data(**num):
    for k,v in num.items():
        print(k,v)
print_data(id=10,s=3)
