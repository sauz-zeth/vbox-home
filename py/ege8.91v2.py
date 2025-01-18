from itertools import product

alpha = 'КАЛИЙ'

def isUnique(p, alpha):
    for x in alpha:
        if p.count(x) != 1:
            return 0

    return 1


n = 0
for p in product(alpha, repeat = 5):
    if isUnique(p, alpha) and p[0] != 'Й' and 'ИА' not in ''.join(p):
        n += 1

print(n)
