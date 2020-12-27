f=open("empp","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n").split(","))
print(lst)