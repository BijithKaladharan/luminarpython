#read data from file named text and display content here
#read
#write
#append

f=open("text","r")
lst=[]

for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)