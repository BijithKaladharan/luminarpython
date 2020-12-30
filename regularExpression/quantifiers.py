#quantifiers

from re import *
#pattern="a+" #check for a and morethan one a
#pattern='a*' #a+ plus zero occurance of a
#pattern='a?'#a plus zero number of a
#pattern='^a'  #chk for starting with 'a'
pattern='a$'  #chk for ending with 'a'
#pattern='a{2,3}' #chk for minimum 2a and maximum 3a
matcher=fullmatch(pattern,"baaaabaabaaaaa")
#for match in matcher:
    #print(match.start())
    #print(match.group())
if matcher!=None:
    print("given string strting with a")
else:
    print("given string is not starting with a")