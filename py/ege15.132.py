def f(x, a):
    nDa = x % a != 0
    nD24 = x % 24 != 0
    nD36 = x % 36 != 0

    return nDa <= (nD24 and nD36)

for a in range(24 * 36, 0, -1):
    if all(f(x, a) for x in range(1, 100)):
        print(a)
        break
