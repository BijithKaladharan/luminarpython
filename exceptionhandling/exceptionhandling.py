#exception

#error
#exception.....abnormal code
lst=[]
no1=int(input("enter value"))
no2=int(input("enter value"))
try:
    res=no1/no2  #10/0  abnormal code that disrupt our normal execution
    print(res)

except Exception as i:
    print(i.args)
try:
    print(lst[5])
except Exception as e:
    print(e.args)
#try.......doubtfulcode
#except......exception handling code