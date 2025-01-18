from itertools import permutations

alpha = 'ВЕНТИЛЬ'

n = 0

for p in set(permutations(alpha, 7)):
    sp = ''.join(p)

    if p[-1] == 'Ь': continue

    if 'ЕЬИ' in sp: continue
    if 'ИЬЕ' in sp: continue

    n += 1

print(n)
