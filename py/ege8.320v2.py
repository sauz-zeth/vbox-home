from itertools import product, combinations

N1 = 10**9
Nfirst0 = 10**8

a = set()
for c in combinations(range(10), 2):
    for p in product(c, repeat = 9):
        if p[0] != 0:
            a.add(p)

print(N1 - Nfirst0 - len(a))
