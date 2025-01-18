from itertools import product

print(*'xyzw')
for p in product(range(2), repeat = 4):
    x, y, z, w = p
    f = ((x <= y) and (y <= w)) or (z == (x or y))
    if not f:
        print(x, y, z, w)
