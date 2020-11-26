def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
digit=factorial(5)
print(digit)
