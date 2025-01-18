from itertools import product

n = 0

for p in product(range(8), repeat = 5):
    if p[4] == 0: continue

    s = '*' + ''.join(map(str, p)) + '*'

    for x in '024':
        s = s.replace(x, '*')

    if '*6*' in s and s.count('6') == 1: 
        n += 1

print(n)
