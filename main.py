#import shuffle from random
from random import shuffle

#import Group
from league import Group

filepath = 'teams.txt'

teams= dict()
with open(filepath) as fp:
   line = fp.readline()
   while line:
       line= line.strip()
       name= line[:line.find(' ')]
       level= eval(line[line.find(' ')+1:])
       teams[name]= level
       line = fp.readline()


#sort the teams by level
teams= sorted(teams.items(), key=lambda x: x[1], reverse=True)


group_teams= [[] for i in range(8)]
for i in range(0, len(teams), 8):
    L= teams[i:i+8]
    shuffle(L)    
    for j in range(8):
        group_teams[j].append(L[j][0])

groups= [Group(group_teams[i]) for i in range(8)]

#GUI

#CUP
