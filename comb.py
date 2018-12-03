from itertools import permutations
from math import cos, sin, pi, sqrt,inf
import timeit

r = 1000  # Given

N = int(input("Enter no of turbines: "))

start = timeit.default_timer()
weight = [i + 1 for i in range(N)]
W = sum(weight)
clist = []

# Excluding an item and Permuting different combinations

for i in permutations(weight[0:N - 1], N - 1):
    clist.append(list(i))

# Adding the combination to the fixed element

for i in clist:
    i.append(weight[-1])
    # print(i)

# Finding the CoG of each solution
S=0
d_min=inf

def getCG(solution_vector):
    n = len(solution_vector)
    Xcg = 0

    Ycg = 0
    global d_min,S

    for i, sln in enumerate(solution_vector):
        # print(sln)
        Xcg = Xcg + r * cos(2 * pi * i / n) * sln
        Ycg = Ycg + r * sin(2 * pi * i / n) * sln

    Xcg /= W
    Ycg /= W
    xlist2 = Xcg**2
    ylist2 = Ycg**2
    d = sqrt(xlist2 + ylist2)

    if d<d_min:
            S=solution_vector
            d_min=d
            # print(d, solution_vector)


for i in clist:
    getCG(i)

print("Minimum Deviation: ", d_min," at ",S,"\n")
stop = timeit.default_timer()

print('Time: ', stop - start)





