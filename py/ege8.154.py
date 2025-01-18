from itertools import product

alpha = 'udlr'
n = 0
for p in product(alpha, repeat = 5):
    if p[0] == 'u' or p == tuple(reversed(p)): continue
    n += 1


print(n)
