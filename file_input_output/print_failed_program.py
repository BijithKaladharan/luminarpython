f1=open("names","r")
f2=open("passed","r")

set1=set()
set2=set()

#def convert_to_set(files):
    #file_set=set()
    #for lines in files:
        #file_set.add(lines.rstrip("\n"))
    #return file_set

#names=convert_to_set(f1)
#passed=convert_to_set(f2)
#result=names-passed
#print(names)
#print(passed)
#print("failed students =",result)

for lines in f1:
    set1.add(lines.rstrip("\n"))
print("name =",set1)
for line in f2:
    set2.add(line.rstrip("\n"))
print("passed =",set2)

result=set1-set2
print("failed =",result)

