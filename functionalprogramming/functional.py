#def add(no1,no2):
    #return no1+no2

# lambda function
# anonymous function(nameless function)
#only possible for single line code

f=lambda no1,no2:no1+no2
print(f(10,30))

f1=lambda no1,no2:no1-no2
print(f1(30,20))

cub=lambda no:no*3
print(cub(2))

even=lambda num:num%2==0
print(even(8))

upper=lambda name:name.upper()
print(upper("hai"))
