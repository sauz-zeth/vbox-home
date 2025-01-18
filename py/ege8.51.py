from itertools import product

alpha = 'КАТЕР'
n = 0

for p in product(alpha, repeat = 5):
    if p.count('Р') >= 2:
        n += 1

print(n)
