from itertools import product

alpha = 'ТИМАШЕВСК'
g = 'ИАЕ'
sg = 'ТМШВСК'

n = 0

for s in map(''.join, product(alpha, repeat = 4)):

    if any('Ш' + x in s or x + 'Ш' in s for x in g): continue

    if sum(s.count(x) for x in g if x in s) == sum(s.count(x) for x in sg if x in s):
        n += 1

print(n)

