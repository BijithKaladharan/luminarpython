llimit=int(input("enter the value"))
hlimit=int(input("enter the value"))
for num in range(llimit,hlimit+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
             print(num)