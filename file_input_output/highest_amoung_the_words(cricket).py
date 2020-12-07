f=open("data","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")

    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)
#........................................method1
#lst=[]
#for k,v in dict.items():
    #lst.append(v)
#high=max(lst)

#for k,v in dict.items():
    #if (v==high):
        #print(k,v)
#.........................................method2

high=max(dict,key=dict.get)
print(high)

