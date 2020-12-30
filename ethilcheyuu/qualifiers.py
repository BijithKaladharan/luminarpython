from re import*
rule='[a-kA-K][369]\w'
variablename=input("enter the variable")
matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("valid")
else:
    print("invlaid")