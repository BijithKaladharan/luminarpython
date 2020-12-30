from re import *
#==========predefined character set============
#pattern='[a-z]' #check for lowercase character
#pattern='[1-9]'  #check forall digit
#pattern='[^0-9]'  #except numbers
#pattern='[^a-z]' #except lowercase characters
#pattern='[a-zA-Z]' #check FOR BOTH LOWER AND UPPERCASE CHARCTERS

#lowercase and uppercase digit
#pattern='[a-zA-Z0-9]'
#special characters only
#pattern='[^a-zA-Z0-9]'

#========predefined characters=========
#pattern="\s"  #checking for spaces
#pattern='\S' #EXCEPT SPACES
#pattern='\d' #checking for digits
#pattern='\D' #EXCEPT DIGITS
pattern='\w' #'[a-zA-Z0-9]
#pattern='\W' #except ^




mather=finditer(pattern,"abc Z@7k")
for match in mather:    #01234567
    print(match.start())#0 1 2 7
    print(match.group())#a b c k