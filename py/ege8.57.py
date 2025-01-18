from itertools import product

alpha = 'ПИРОГ'
n = 0

for p in product(alpha, repeat = 6):
    s = ''.join(p)
    if ('РИ' in s or 'РО' in s) and s.count('Р') == 1:
        n += 1

print(n)
