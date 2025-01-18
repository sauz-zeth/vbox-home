from itertools import combinations
from math import prod

summ = 0

for c in combinations(range(10), 5):
    a = bytearray([4]) * 10
    for i in c:
        a[i] = 1
    
    if bytes([1, 1]) in a: continue

    if a[0] == 4:
        a[0] = 3

    summ += prod(a)

print(summ)
