from itertools import product

salpha = 'КРШ'
galpha = 'ЫА'
alpha = 'КРЫША'

n = 0

for l in range(3, 5 + 1):
    for p in product(alpha, repeat = l):
        
        if all(c not in p[1:] for c in salpha):
            if all(p.count(c) <= 2 for c in galpha):
                n += 1
print(n)

