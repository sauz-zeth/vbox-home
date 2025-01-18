from itertools import product

alpha = 'ЖИРАФ'
n = 0

for p in product(alpha, repeat = 6):
    if 1 <= p.count('А') <= 4:
        n += 1

print(n)
