from itertools import product

g = (tuple(sorted(p)) for p in product(range(16), repeat = 5))

print(len(set(p for p in g if p[0] != 0)))
