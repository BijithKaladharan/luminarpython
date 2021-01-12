# def sub(num1,num2):
#     #if a condition given we cannot use num1,num2=num2,num1 using if....so in this case we use decarotor
#     return num1-num2

def sub_dec(func):
    def wrap(no1,no2):
        if no1<no2:
            no1,no2=no2,no1
        return func(no1,no2)
    return wrap
@sub_dec
def sub(num1,num2):
    #if a condition given we cannot use num1,num2=num2,num1 using if....so in this case we use decarotor
    return num1-num2



res=sub(40,60)
print(res)
