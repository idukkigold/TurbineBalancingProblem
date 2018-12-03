import numpy as np
import timeit
from math import cos, pi,inf

n = int(input(" Enter turbine count: "))
weight = [i + 1 for i in range(n)]


def Cal_MinSlot(Current_config,n,c):
    D = []


    for i,slot in enumerate(Current_config):
        Temp_config = Current_config[:]
        if slot==0:

            Temp_config[i]=c
            current_dev = 0
            constraint = 0
            for j,tempslot in enumerate(Temp_config):
                current_dev+= weight[j]*cos(2*pi*(i-j)/n)
            D.append(current_dev)
            print(Temp_config,current_dev)

        else:D.append(inf)

    p=np.argmin(D)

    return p


def PlaceTurbine():
    # fix slots '0' for open, '1' for placed
    Slots = [0 for i in range(n - 1)]
    Slots.append(1)
    Slots.reverse()
    W = np.sum(sum(weight))
    Current_config = Slots
    print(Current_config)

    i=2
    Final_config=Current_config

    print("Starting Configuration: ",Final_config)
    start = timeit.default_timer()

    while i!=n+1:

        minSlot=Cal_MinSlot(Current_config,n,i)
        print("Found minSlot at : ",minSlot)
        Final_config[minSlot] = i
        print("Final :",Final_config)
        i+=1

    stop = timeit.default_timer()

    print("Time for execution :",stop-start,"s")

def main():
    PlaceTurbine()

if __name__ == "__main__":
    main()


