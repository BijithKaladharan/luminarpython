n=int(input("enter value"))
min=int(input("enter the number"))
max=int(input("enter the number"))

for i in range(1,max+1):
    if i**n in range(min,(max+1)):
        print(i,",",i**n)