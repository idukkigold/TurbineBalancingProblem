import numpy as np
from itertools import  permutations
from collections import Counter
import timeit
from math import cos, sin, pi, sqrt,fabs

start = timeit.default_timer()
n= int (input(" Enter turbine count: "))
weight = [i + 1 for i in range(n)]


#fix slots 0 for open 1 for placed
Slots= [0 for i in range(n-1)]
Slots.append(1)
Slots.reverse()

W = sum(weight)
Current_config=Slots

def Cal_MinSlot(Current_config):
    k=Current_config.count(1)
    print(k)

    # return minSlot


def PlaceTurbine():
    while 0 not in Current_config:
        minSlot=Cal_MinSlot(Current_config)
        Current_config[minSlot] = 1

Cal_MinSlot(Current_config)