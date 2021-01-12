s=[]

while True:
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4 .EXIT")
    choice=int(input("enter your choice:"))
    if(choice==1):
        size=int(input("enter the size of the stack"))
        for j in range(size):
            a=input("enter the element:")
            s.append(a)
    elif(choice==2):
        if s==[]:
            print("  ...under flow... \n cannot pop element")
        else:
            print("element poped-",s.pop())
    elif(choice==3):
        print("*"*10)
        for i in range(len(s)-1,-1,-1):

            print(s[i])
        print("*"*20)
    elif(choice==4):
        break
    else:
        print("invalid choice....")