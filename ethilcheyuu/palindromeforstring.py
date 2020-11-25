#if imagine given string is abcde
#print(str[:])   ---->#abcde
#print(str[0:5])   ---->#abcde----->ie starting point and ending point specified
#print(str[0:5:1]) ---->#abcde------>ie starting point ending point and increment point
#print(str[::])  ---->#abcde----->defaulty assing as above
#print(str[::-1]) ---->#edcba------>reverse order

str=input("enter the string")
revstr=(str[::-1])

if (revstr==str):
    print("palindrome")
else:
    print("not palindrome")

