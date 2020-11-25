num=int(input("enter the value"))
fact=1
if num==0:
    print(1)
elif num<0:
    print("invalid")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)