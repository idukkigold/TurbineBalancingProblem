import numpy as np
import timeit
from math import cos, pi

start = timeit.default_timer()
n= int (input(" Enter turbine count: "))
weight = [i + 1 for i in range(n)]

k=10000
p=0

#fix slots 0 for open 1 for placed
Slots= [0 for i in range(n-1)]
Slots.append(1)
Slots.reverse()


W = np.sum(sum(weight))
Current_config=Slots
minSlot=0

def Cal_MinSlot(Current_config):
    Temp_config = Current_config
    global p, k
    for i,slot in enumerate(Temp_config):
        if slot==1:
            continue
        else:
            Temp_config[i]=1

            for j,tempslot in enumerate(Temp_config):
                constraint= j*cos(2*pi*(i-j)/n)
                if constraint<k:
                    k=constraint
                    p=i

    return p




    # return minSlot


def PlaceTurbine():
    c=1
    Final_config=Current_config
    while c!=n:
        minSlot=Cal_MinSlot(Final_config)
        Final_config[minSlot] = c
        c+=1

    print(Final_config)

PlaceTurbine()

