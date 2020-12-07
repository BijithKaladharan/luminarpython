f=open("b","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(",")
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)
lst=[]

for k,v in dict.items():
    lst.append(v)
high=max(lst)
print(high)
for k,v in dict.items():
    if v==high:
        print(k,v)


