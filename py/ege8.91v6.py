from itertools import permutations

alpha = 'КАЛИЙ'

n = 0
for p in permutations(alpha):
    if p[0] != 'Й' and 'ИА' not in ''.join(p):
        n += 1

print(n)
