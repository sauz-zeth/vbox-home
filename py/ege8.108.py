from itertools import permutations

alpha = 'КОМЕТА'
s = 'КМТ'
g = 'ОЕА'

n = 0

def ok(sp):
    for l in permutations(s, 2):
        if ''.join(l) in sp: return False

    for k in permutations(g, 2):
        if ''.join(k) in sp: return False

    return True

for p in permutations(alpha, 6):
    sp = ''.join(p)

    if ok(sp):
        n += 1

print(n)
