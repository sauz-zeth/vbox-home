from itertools import product

alpha = 'UDRL'
n = 0

for p in product(alpha, repeat = 5):
    if p[0] != 'U' and p[0] != p[2] and p[1] != p[3] and p[2] != p[4]:
        n += 1

print(n)
