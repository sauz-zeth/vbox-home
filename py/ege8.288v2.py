from itertools import product

alpha = 'ТИМАШЕВСК'
alpha_ = 'sgsgШgsss'

n = 0
for s in map(''.join, product(alpha_, repeat = 4)):
    if 'Шg' in s or 'gШ' in s: continue

    if s.count('g') == s.count('s') + s.count('Ш'):
        n += 1

print(n)

