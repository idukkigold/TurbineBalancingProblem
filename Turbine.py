import numpy as np
from itertools import  permutations
import timeit
from math import cos, sin, pi, sqrt,fabs


n= int (input(" Enter turbine count: "))






#fix slots 0 for open 1 for placed
Slots= [0 for i in range(n-1)]
Slots.append(1)
Slots.reverse()

Current_config=[]

def Cal_MinSlot(Current_config):

    minSlot=1

    return minSlot


def PlaceTurbine():

    while 0 not in Current_config:
        minSlot=Cal_MinSlot(Current_config)
        Current_config[minSlot]=1