lst=int(input("enter the limit"))
odd=[]
even=[]
for i in range(1,lst+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)