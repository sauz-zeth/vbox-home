from itertools import product

alpha = 'UDRL'
n = 0

for p in product(alpha, repeat = 4):
    if p[0] != 'U' and p[1] != p[2]:
        n += 1

print(n)
