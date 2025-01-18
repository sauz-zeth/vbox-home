from itertools import product
alpha = 'СМОКАТ'

n = 0
for s in map(''.join, product(alpha, repeat = 7)):
    if 'АСАМА' in s or 'ОСАМО' in s:
        n += 1

print(n)
