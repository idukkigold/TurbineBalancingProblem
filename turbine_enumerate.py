r=10000 #Given


from itertools import permutations
weight=[i+1 for i in range(10)]

W=sum(weight)
clist=[]

#Excluding an item and Permuting different combinations
for i in permutations(weight[0:9],9):
    clist.append(list(i))

#Adding the combination to the fixed element
for i in clist:
    i.append(10)

#Finding the CoG of each solution
import math



def getCG(solution_list):
    n=len(solution_list)
    Xcg=0
    Ycg=0

    for sln in solution_list:

        pass











