num=int(input("enter the number"))
total=0
while(num!=0):
    digit=num%10#3#2
    total=total+(digit**3)#27#27+8=35

    num=num//10#12#1
print(total)#27


