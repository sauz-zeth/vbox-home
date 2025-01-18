from itertools import product

alpha = 'КАЛИЙ'

n = 0
for p in product(alpha, repeat = 5):
    if any(p.count(x) != 1 for x in alpha): continue

    if p[0] != 'Й' and 'ИА' not in ''.join(p):
        n += 1

print(n)
