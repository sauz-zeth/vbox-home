def f(x, a):
    return (x & 25 != 1) or ((x & 34 == 2) <= (x & a == 0))

for a in range(1, 100):
    if all(f(x, a) for x in range(1, 100)):
        print(a)
        break
