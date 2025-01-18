from itertools import product

print(*'xyzw')
for p in product(range(2), repeat  = 4):
    x, y, z, w = p
    f = (w <= z) and ((y <= x) == (z <= y))
    if f:
        print(x, y, z, w)
