# TurbineBalancingProblem
Enumeration and heuristic procedure for the turbine balancing problem in Python


Heuristics:

Step 1 (Initialization). Place Blade 1 in Position
1. Let P = {2, 3 . . . . . n) be the current set of available
(unoccupied) positions. Go to Step 2.
general Step k (for k = 2 to n). Place Blade k
in Position j* such that
k-I
Y'~ w i cos{Zw[j*-l(i)]/n}
i-1
k-I
= minimum E w, cos{2~r[j - l ( i ) ] / n }
J~P i=1
where l(i)=Position of Blade i, for i= 1 to
k- 1. Let P = P\j*. If k = n, stop; otherwise go
to Stepk+l.
The computational requirement of the Placement
Heuristic is of order n 3.
