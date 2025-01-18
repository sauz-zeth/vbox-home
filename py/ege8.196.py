from itertools import product

salpha = 'КРШ'
galpha = 'ЫА'
alpha = 'КРЫША'

def s(p):
    for c in salpha:
        for i in range(1, len(p)): 
            if p[i] == c:
                return True
    return False

def g(p):
    for c in galpha:
        if ''.join(p).count(c) > 2:
            return True
    return False


n = 0

for l in range(3, 5 + 1):
    for p in product(alpha, repeat = l):
        
        if s(p) or g(p): continue 
        n += 1

print(n)

