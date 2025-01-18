from itertools import permutations

alpha = 'СГСГСГ'

n = 0

for p in permutations(alpha, 6):
    sp = ''.join(p)

    if 'СС' in sp or 'ГГ' in sp: continue

    n += 1

print(n)
