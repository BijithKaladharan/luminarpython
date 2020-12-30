from re import *
f=open("emails","r")
fout=open("valid_email","w")
ems=set()
for mails in f:
    ems.add(mails.rstrip("\n"))

rule="[a-zA-Z0-9.-_]*gmail.com"
for s in ems:
    matcher=fullmatch(rule,s)
    if matcher!=None:
        fout.write(s+"\n")
    else:
        pass