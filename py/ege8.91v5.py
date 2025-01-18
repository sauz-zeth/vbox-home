from itertools import product

alpha = 'КАЛИЙ'

n = 0
for p in product(alpha, repeat = 5):
    if len(set(p)) != 5: continue

    if p[0] != 'Й' and 'ИА' not in ''.join(p):
        n += 1

print(n)
