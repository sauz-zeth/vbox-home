from itertools import permutations
from math import prod

alpha = '7' * 5 + '1' * 5

summ = 0

for p in set(permutations(alpha)):
    s = ''.join(p)

    if '11' in s: continue

    s = s.replace('17', '14')
    s = s.replace('71', '41')

    if s[0] == '7':
        s = '6' + s[1:]

    if s[0] == '4':
        s = '3' + s[1:]

    pr = prod(map(int, s))
    summ += pr

print(summ)
