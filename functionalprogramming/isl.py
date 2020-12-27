from functools import *
isl=[
    {"team_name":"mumbaicity","mp":7,"win":5,"draw":1,"loss":1,"gf":11,"ga":3,"pts":16},
    {"team_name":"atk","mp":7,"win":5,"draw":1,"loss":1,"gf":8,"ga":3,"pts":16},
    {"team_name":"benguluru","mp":7,"win":3,"draw":3,"loss":1,"gf":11,"ga":8,"pts":12},
    {"team_name":"northeast","mp":7,"win":2,"draw":4,"loss":1,"gf":8,"ga":6,"pts":10},
    {"team_name":"jemshedh","mp":7,"win":2,"draw":4,"loss":1,"gf":8,"ga":7,"pts":10}

]

#print all team name in upper case

teams=list(map(lambda team:team["team_name"].upper(),isl))
print(teams)

#print highest points

point=reduce(lambda p1,p2:p1 if p1>p2 else p2,
             list(map(lambda team:team["pts"],isl)))
team=list(filter(lambda team:team["pts"]==point,isl))
print(team)

