from itertools import product

#_alpha = 'КОНФЕТА'
alpha = 'sgssgsg'

n = 0
for s in map(''.join, product(alpha, repeat = 5)):
    if all('s' in x for x in s.split('g')[1:-1]) and s.count('g') >= 2:
        n += 1

print(n)
