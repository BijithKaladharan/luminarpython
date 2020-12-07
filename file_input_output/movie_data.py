f=open("movie_data","r")
dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")

    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict["1992"])

#which year highest number of movies released

high=max(dict,key=dict.get)
print(high,dict[high])
