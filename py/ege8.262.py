from itertools import product

def ok(p):
    s = '*' + ''.join(map(str, p)) + '*'
    for i in '0246*':
        for j in '0246*':
            if i + '6' + j in s:
                return True
    return False

n = 0

for p in product(range(8), repeat = 5):
    if p[4] == 0: continue

    if p.count(6) == 1 and ok(p):
        n += 1

print(n)
