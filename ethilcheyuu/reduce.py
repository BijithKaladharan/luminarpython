from functools import *
lst=[10,11,12,13,14,15,2,16,17,18]
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(filter(lambda no:no%2==0,lst)))
print(min)
