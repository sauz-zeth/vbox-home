from itertools import permutations

alpha = 'АДЖИКА'

n = 0

for p in set(permutations(alpha, 6)):
    if 'АА' in ''.join(p): continue

    n += 1

print(n)
