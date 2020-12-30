#import re
#p=re.finditer("ab","abababababaabbab")
#cnt=0
#for i in p:
    #print(i.start())
    #print(i.start())
    #cnt+=1
#print(cnt)

from re import*
pattern='\S'
matcher=finditer(pattern,"abc Z@7k")
#for match in matcher:
    #print(match.start())
    #print(match.group())

out=[(match.start(),match.group()) for match in matcher]
print(out)