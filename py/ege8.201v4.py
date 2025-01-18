from itertools import product

n = 0

for p in product(range(16), repeat = 5):
    if 0 < p[4] <= p[3] <= p[2] <= p[1] <= p[0]:
        n += 1

print(n)
