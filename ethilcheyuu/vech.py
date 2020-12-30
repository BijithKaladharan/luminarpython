from re import *
f=open("vechiclereg","r")
fout=open("validreg","w")
regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))

rule='KL\d{2}[A-Z]{2}\d{1,4}'
for vechnum in regnum:
    matcher=fullmatch(rule,vechnum)
    if matcher!=None:
        fout.write(vechnum+"\n")
    else:
        pass