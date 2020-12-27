from functools import *

#reduce

#randu element randu element vecha annu function work cheyune..10,11...pinne 11,12...pinne 12,13.....
lst=[10,11,12,13,14,15,16,17,18]

#sum
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

#min

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)

#max
max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)
# find min of even no from this list
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(filter(lambda no:no%2==0,lst)))
print(min)