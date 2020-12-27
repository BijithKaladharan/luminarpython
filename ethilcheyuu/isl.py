from functools import *
isl=[
    {"team_name":"mumbaicity","mp":7,"win":5,"draw":1,"loss":1,"gf":11,"ga":3,"pts":16},
    {"team_name":"atk","mp":7,"win":5,"draw":1,"loss":1,"gf":8,"ga":3,"pts":40},
    {"team_name":"benguluru","mp":7,"win":3,"draw":3,"loss":1,"gf":11,"ga":8,"pts":12},
    {"team_name":"northeast","mp":7,"win":2,"draw":4,"loss":1,"gf":8,"ga":6,"pts":10},
    {"team_name":"jemshedh","mp":7,"win":2,"draw":4,"loss":1,"gf":8,"ga":7,"pts":10}

]

upp=list(map(lambda x:x["team_name"].upper(),isl))
print(upp)

h=reduce(lambda n1,n2:n1 if n1>n2 else n2,list(map(lambda n:n["pts"],isl )))
print(h)

wh=reduce(lambda r1,r2:r1 if r1>r2 else r2,list(map(lambda v:v["win"],isl)))
print(wh)
det=list(filter(lambda d:d["win"]==wh,isl))
print(det)