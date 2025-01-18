from itertools import permutations

alpha = 'хочу в вуз'

n = 0

for p in set(permutations(alpha)):
    s = ' ' + ''.join(p)
    if ' ' + ' ' in s: continue
    if s[-1] == ' ': continue
    if ' у' in s: continue

    n += 1

print(n - 1)
