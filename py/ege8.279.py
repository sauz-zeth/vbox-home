from itertools import permutations

alpha = 'ЭФЕКТ'

n = 0

for p in permutations(alpha, 5):
    if p.index('Е') < p.index('Э') and p.index('К') < p.index('Т') < p.index('Ф'):
        n += 1
#        print(p)

print(n)

