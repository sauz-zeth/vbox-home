from itertools import product

def f(x, y, z):
    return (x <= (not z)) and ((not y) <= x)

print(*'xyzf')
for p in product(range(2), repeat = 3):
    x, y, z = p
    print(x, y, z, int(f(*p)))
