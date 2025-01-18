def f(x, a):
    return (x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))

for a in range(1, 100):
    if all(f(x, a) for x in range(1, 100)):
        print(a)
        break
