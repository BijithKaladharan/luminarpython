f=open("text","r")
set=set()

for lines in f:
    set.add(lines.rstrip("\n"))
print(set)