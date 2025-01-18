from itertools import product

print('a b c f')
for p in product(range(2), repeat = 3):
    a, b, c = p
    f = not a or (b and not c)
    print(*p, int(f))
