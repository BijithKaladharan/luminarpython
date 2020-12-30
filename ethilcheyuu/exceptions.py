no1=int(input("enter the value no1"))
no2=int(input("enter the value no2"))
try:
    res=no1/no2
    print(res)
except:
    no2=int(input("enter the value no2"))
    try:
        res=no1/no2
        print(res)
    except:
        no2 = int(input("enter the value no2"))
        res=no1/no2
        print(res)
finally:
    # res=no1/no1+1
    # print(res)
    print("invlid")