def sub_dec(func):
    def wrap(no1,no2):
        if no1<no2:
            no1,no2=no2,no1
        return func(no1,no2)
    return wrap
@sub_dec

def div(num1,num2):
    return num1/num2

data=div(2,10)
print(data)