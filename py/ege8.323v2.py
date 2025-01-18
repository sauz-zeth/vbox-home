from itertools import permutations
from math import prod

alpha = '4' * 5 + '1' * 5

summ = 0

for p in set(permutations(alpha)):
    s = ''.join(p)

    if '11' in s: continue

    if s[0] == '4':
        s = '3' + s[1:]

    print(s)

    pr = prod(map(int, s))
    summ += pr

print(summ)
