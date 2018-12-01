import numpy as np
import timeit
from math import cos, pi

n = int(input(" Enter turbine count: "))
weight = [i + 1 for i in range(n)]


def Cal_MinSlot(Current_config,n):

    constraint = 0
    p = 0
    for i,slot in enumerate(Current_config):
        Temp_config = Current_config[:]

        if slot==0:
            Temp_config[i]=1
            print("Temo: ",Temp_config)

            for j,tempslot in enumerate(Temp_config):
                if j==0:
                    constraint= weight[j]*cos(2*pi*(i-j)/n)
                    p=0
                    continue

                else:
                    k=weight[j]*cos(2*pi*(i-j)/n)
                    # print(i,j,constraint)
                    if k<constraint:
                        p=i
    return p

def PlaceTurbine():


    # fix slots '0' for open, '1' for placed
    Slots = [0 for i in range(n - 1)]
    Slots.append(n)
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
        print("Final :",Final_config)
        c+=1

    print(Final_config)
    stop = timeit.default_timer()

    print("Time for execution :",stop-start,"s")

def main():
    PlaceTurbine()

if __name__ == "__main__":
    main()


