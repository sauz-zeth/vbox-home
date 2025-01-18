from itertools import product

alpha = 'КАЛИЙ'

def isUnique(p, alpha):
    return all(p.count(x) == 1 for x in alpha)

n = 0
for p in product(alpha, repeat = 5):
    if isUnique(p, alpha) and p[0] != 'Й' and 'ИА' not in ''.join(p):
        n += 1

print(n)
