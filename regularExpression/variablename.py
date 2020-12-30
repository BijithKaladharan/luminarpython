#variable name rule
#starting with a-k
#second charcter should be a digit and it must be divisible by 3
#followed by any number of characters
#z2rggg=>invlaid
#B7vggg=>invlaid
#a3rgggg=>valid

from re import *
rule='[a-kA-K][369][a-zA-Z0-9]'

variablename=input("enter the varaible name")
matcher=match(rule,variablename)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")