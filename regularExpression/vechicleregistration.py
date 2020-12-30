#kl08bn4970->invalid
#KL08BS1375->VALID
#GJ0BBN2211=>INVALID
f=open("registrationnumbers","r")
fout=open("validregistrationnumber","w")
regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))


from re import *
rule='KL\d{2}[A-Z]{1,2}\d{1,4}'

for vechiclenum in regnum:

    matcher=fullmatch(rule,vechiclenum)
    if matcher!=None:
        fout.write(vechiclenum+"\n")
    else:
        pass


#create rule for validating e mail id
#validate all phone numbers-