from itertools import product

alpha = 'ЛЕТО'
n = 0

for p in product(alpha, repeat = 5):
    if 'Е' in ''.join(p):
        n += 1

print(n)
