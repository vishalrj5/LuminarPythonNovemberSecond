from functools import *

isl=[
    {"team":"mumbaicity","mp":7,"win":5,"drawn":1,"loss":1,"gf":11,"ga":3,"pts":16},
    {"team":"atk","mp":7,"win":5,"drawn":1,"loss":1,"gf":8,"ga":3,"pts":16},
    {"team":"benguluru","mp":7,"win":3,"drawn":3,"loss":1,"gf":11,"ga":8,"pts":12},
    {"team":"northeast","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":6,"pts":10},
    {"team":"jemshedh","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":7,"pts":10}

]

#print all team name in uppercase
teams=list(map(lambda team:team["team"].upper(),isl))
print(teams)

#print highest point
highest=reduce(lambda p1,p2:p1 if p1>p2 else p2,
               list(map(lambda team:team["pts"],isl))
               )
print(highest,"is the highest point")

tea=list(filter(lambda tea:tea["pts"]==highest,isl))
print(tea)

#find minimum points
minimum=reduce(lambda p1,p2:p1 if p1<p2 else p2,
               list(map(lambda min:min["pts"],isl)))
print(minimum,"is the minimum score")
#highest win team
win=reduce(lambda w1,w2:w2 if w1<w2 else w1,
           list(map(lambda wind:wind["win"],isl))
           )
hteam=list(filter(lambda h1:h1["win"]==win,isl))
print(hteam)
