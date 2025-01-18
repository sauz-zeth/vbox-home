from itertools import product

n = 0

for p in product(range(16), repeat = 5):
    if p[0] == 0: continue

    if p == tuple(sorted(p)):
        n += 1

print(n)
