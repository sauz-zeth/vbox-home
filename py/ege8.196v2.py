from itertools import product

salpha = 'КРШ'
galpha = 'ЫА'
alpha = 'КРЫША'

def s(p):
    for c in salpha:
        if c in p[1:]:
            return False
    return True


def g(p):
    for c in galpha:
        if p.count(c) > 2:
            return False
    return True


n = 0

for l in range(3, 5 + 1):
    for p in product(alpha, repeat = l):
        
        if s(p) and g(p): 
            n += 1

print(n)

