from itertools import product

print(*'xyzwf')
for p in product(range(2), repeat = 4):
    x, y, z, w = p
    f = x and (y and z or z and w or y and not w)
    if f:
        print(*p, int(f))
