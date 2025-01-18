from itertools import product

alpha = 'АИКЛМЬ'

a = [p for p in product(alpha, repeat = 6)]

for p in a:
    if p[0] == 'К' and p[-1] == 'Ь' and all(p.count(x) == 1 for x in p):
        if a.index(tuple(reversed(p))) - a.index(p) == 26655:
            print(sum(int(x) for x in str(a.index(p) + 1)))
            break
