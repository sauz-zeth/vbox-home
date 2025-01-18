from itertools import permutations
from math import prod

alpha = [4] * 5 + [1] * 5

summ = 0

for p in set(permutations(alpha)):
    a = list(p)
    s = ''.join(map(str, a))

    if '11' in s: continue

    if a[0] == 4:
        a[0] = 3

    summ += prod(a)

print(summ)
