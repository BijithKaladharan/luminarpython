llimit=int(input("enter the limit"))
hlimit=int(input("enter the limit"))
sumodd=0
sumeven=0
while(llimit<=hlimit):
    if(llimit%2==0):
        sumeven=sumeven+llimit
    else:
       sumodd=sumodd+llimit
    llimit=llimit+1
print("sumodd is",sumodd)
print("sumeven is ",sumeven)
