from itertools import permutations

alpha = 'ВОРОТА'

n = 0

for p in set(permutations(alpha, 6)):
    sp = ''.join(p)

    if 'ОО' in sp: continue
    if 'ОА' in sp: continue
    if 'АО' in sp: continue

    n += 1

print(n)
