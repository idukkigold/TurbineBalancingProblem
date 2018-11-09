r=10000 #Given


from itertools import permutations
weight=[i+1 for i in range(10)]
s=[]

#Excluding an item and Permuting different combinations
for i in permutations(weight[0:9],9):
    s.append(list(i))

#Adding the combination to the fixed element
for i in s:
    i.append(10)
    print(i)

#Finding the CoG of each solution
for i,solution in enumerate(s):
    #function to generate distance
    pass





