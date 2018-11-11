r = 10000  # Given

from itertools import permutations
from math import cos, sin, pi, sqrt

N = int(input("Enter no of turbines: "))

weight = [i + 1 for i in range(N)]
W = sum(weight)
clist = []

# Excluding an item and Permuting different combinations

for i in permutations(weight[0:N - 1], N - 1):
    clist.append(list(i))

# Adding the combination to the fixed element

for i in clist:
    i.append(weight[-1])
    print(i)

# Finding the CoG of each solution
xlist = []
ylist = []


def getCG(solution_vector):
    n = len(solution_vector)
    Xcg = 0
    Ycg = 0

    for i, sln in enumerate(solution_vector):
        # print(sln)
        Xcg = Xcg + r * cos(2 * pi * i / n) * sln
        Ycg = Ycg + r * sin(2 * pi * i / n) * sln

    Xcg /= W
    Ycg /= W

    xlist.append(Xcg)
    ylist.append(Ycg)

    print(Xcg, Ycg)


for sln in clist:
    getCG(sln)

xlist2 = [i * i for i in xlist]
ylist2 = [i * i for i in ylist]

d_min = sqrt(xlist2[0] + ylist2[0])
a = 0
for i, j in zip(xlist2, ylist2):
    d = sqrt(i + j)
    if d < d_min:
        d_min = d
        a += 1

    print(sqrt(i + j))

print("Minimum Deviation: ",clist[a],"\n", d_min)







