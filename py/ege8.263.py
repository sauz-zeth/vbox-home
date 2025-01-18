from itertools import product

n = 0
for p in product(range(9), repeat = 5):
    if p[0] == 0: continue
    if p[0] % 2 != 0: continue
    if p[-1] == 1 or p[-1] == 8: continue
    if p.count(3) > 1: continue

    n += 1

print(n)
