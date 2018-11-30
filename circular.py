import numpy as np
import timeit
from math import cos, pi
from itertools import cycle

n = int(input(" Enter turbine count: "))
weight = [i + 1 for i in range(n)]

    # fix slots 0 for open 1 for placed
Slots = [0 for i in range(n - 1)]
Slots.append(1)
Slots.reverse()
W = np.sum(sum(weight))
Current_config = Slots

turbine=cycle(Current_config)

for slot in turbine:
    if slot==1:
        continue
    else:
        temp turbine=turbine
