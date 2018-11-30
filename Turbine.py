import numpy as np
import timeit
from math import cos, pi

def Cal_MinSlot(Current_config,n):
    Temp_config = Current_config[:]
    constraint = 0
    p = 0
    for i,slot in enumerate(Temp_config):

        if slot==0:
            Temp_config[i]=1


            for j,tempslot in enumerate(Temp_config):
                if j==0:
                    constraint= j*cos(2*pi*(i-j)/n)
                    p=0
                    continue

                else:
                    k=j*cos(2*pi*(i-j)/n)
                    if k<constraint:
                        p=i
    return p

def PlaceTurbine():
    n = int(input(" Enter turbine count: "))
    weight = [i + 1 for i in range(n)]

    # fix slots 0 for open 1 for placed
    Slots = [0 for i in range(n - 1)]
    Slots.append(1)
    Slots.reverse()
    W = np.sum(sum(weight))
    Current_config = Slots
    print(Current_config)

    c=1
    Final_config=Current_config

    print("Starting Configuration: ",Final_config)
    start = timeit.default_timer()

    while c!=n:

        minSlot=Cal_MinSlot(Current_config,n)
        print("Found minSlot at : ",minSlot)
        Final_config[minSlot] = c
        print(c)
        c+=1

    print(Final_config)
    stop = timeit.default_timer()

    print("Time for execution :",stop-start,"s")

def main():
    PlaceTurbine()

if __name__ == "__main__":
    main()


