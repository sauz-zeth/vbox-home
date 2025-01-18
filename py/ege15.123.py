def f(x, a):
    D18 = x % 18 == 0
    NDa = x % a != 0
    ND12 = x % 12 != 0

    return D18 <= (NDa <= ND12)

for a in range(1000, 0, -1):
    if all(f(x, a) for x in range(1, 1000)): break

print(a)


