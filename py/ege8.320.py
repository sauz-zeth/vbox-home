from itertools import product

n = 0

for p in product(range(10), repeat = 9):
    if p[0] != 0:
        if len(set(p)) >= 3:
            n += 1

print(n)
