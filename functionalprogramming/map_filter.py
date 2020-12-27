#map()
#filter()
#reduce()

#lst=[10,11,12,13,14,15]
#calculate square of each number

#squares
#map(function,iterable)

#  def sq(num):
#    return num**2

#   squares=list(map(sq,lst))
#    print(squares)

#   res=list(map(lambda num:num**2,lst))
#   print(res)

#............................................................
#filter

#   even=list(filter(lambda num:num%2==0,lst))
#   print(even)

#............................................................


#convert to upper case
employees=["ajay","vijay","anil","danie","tom","joy"]
upper=list(map(lambda name:name.upper(),employees))
print(upper)

#print all name starting with a
enames=list(filter(lambda name:name[0]=='a',employees))
print(enames)
