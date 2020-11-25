num=int(input("enter the number"))
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(temp==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")