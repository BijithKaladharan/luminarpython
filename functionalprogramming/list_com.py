#first=[1,2,3,]
#second=[4,5,6]

#(1,4)(1,5)(1,6)(2,4)(2,5)(2,6)(3,4)(3,5)(3,6)

#for i in first:
    #for j in second:
        #print(i,j)
#pairs=[(i,j) for i in first for j in second]
#print(pairs)

#square

#squares=[i**2  for i in first]
#print(squares)

#first=[1,2,3,5,6,7]
#data=[i-1 if i<5 else i+1 for i in first]
#print(data)

#lst=[1,2,3,4,5,6,7,8]

#data=[i+1 if i>5 else i-1 if i<5 else 5 for i in lst]
#print("output",data)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#1,2,3,4,5,6,7,8,9
flat=[j for i in matrix for j in i]
print(flat)
     #for i in matrix:
         #for j in i:
             #print(j)
