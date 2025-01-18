from itertools import product

n = 0
for p in product('МАРТ', repeat = 6):
    if p.count('Р') == 2:
        n += 1
print(n)
    

