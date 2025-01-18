from itertools import product

alpha = 'МООСОЙ'
n = 0

for p in product(alpha, repeat = 4):
    if p[0] != 'Й' and 'О' in p:
        n += 1

print(n)
