from itertools import product

alpha = 'КАЛИЙ'
n = 0

for p in product(alpha, repeat = 5):
    fl = 0
    for x in alpha:
        if p.count(x) != 1:
            fl = 1
            break
    if fl == 1: continue
    
    if p[0] != 'Й' and 'ИА' not in ''.join(p):
        n += 1

print(n)
