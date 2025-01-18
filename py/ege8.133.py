from itertools import permutations

alpha = 'ЗДАНАА'
n = 0

for p in permutations(alpha, 6):
    if 'АА' in ''.join(p): continue
    n += 1

print(n)

