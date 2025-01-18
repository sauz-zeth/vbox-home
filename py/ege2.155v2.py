from itertools import product

print(*'xyzf')
for p in product(range(2), repeat = 3):
    x, y, z = p

    f = (x <= (not z)) and ((not y) <= x)

    print(x, y, z, int(f))
