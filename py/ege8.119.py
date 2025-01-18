from itertools import permutations
alpha = 'МАГИСТР'

n = 0
for p in permutations(alpha, 5):
    if 'А' in p and 'И' in p: continue
    n += 1

print(n)

