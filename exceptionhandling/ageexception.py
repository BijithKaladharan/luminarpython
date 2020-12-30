#age<18
# age=int(input("enter age"))
# if age<18:
#     raise Exception("sorry invalid age") #custamised exception by using keyword raise



num=input("enter the value")
if type(num)!=int:
    raise Exception("only integrs allowed")
