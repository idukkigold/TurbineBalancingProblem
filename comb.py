


def get_cyclics(p, k):
  found = set()      # set of tuples we have seen so far
  todo = [tuple(p)]  # list of tuples we still need to explore
  n = len(p)
  while todo:
    x = todo.pop()
    for i in range(n - k + 1):
      perm = ( x[:i]                    # Prefix
             + x[i+1:i+k] + x[i:i+1]    # Rotated middle
             + x[i+k:]                  # Suffix
             )
      if perm not in found:
        found.add(perm)
        todo.append(perm)
  for x in found:
    print(x)


k=2
p=[1,2,3,4]

get_cyclics(p,2)

