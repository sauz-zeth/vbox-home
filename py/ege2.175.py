from itertools import product

print('x y z')
for p in product(range(2), repeat = 3):
    x, y, z = p
    f = (z or y) <= (x == z)

    if not f:
        print(x, y, z)
