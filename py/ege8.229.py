from itertools import product

n = 0
for p in product(range(7), repeat = 7):

    if p[0] == 0 or p[0] == 3 or p[0] == 5: continue

    s = ''.join(map(str, p))
    if '22' in s and '44' in s: continue

    n += 1

print(n)

