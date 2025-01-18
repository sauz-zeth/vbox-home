from itertools import product

alpha = 'АТИТУТ'
n = 0

for p in product(alpha, repeat = 6):
    if p.count('Т') >= 3:
        n += 1

print(n)

