class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a,b,c):
        s=a+b+c
        return s

s1=student(32,78)

print(s1.sum(5,9,3))
s2=student(1,3)
print(s2.sum(10,3,7))