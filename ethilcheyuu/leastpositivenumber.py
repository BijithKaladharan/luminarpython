lis=[-2,-1,0,1,2,3,4]
cnt=1
for i in lis:
    if cnt in lis:
        cnt=cnt+1
    else:
        print(cnt,"is the missing +ve interger number")
        break