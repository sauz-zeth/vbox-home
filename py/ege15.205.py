def f(x, a):
    Za = x & a == 0
    Z31 = x & 31 == 0
    Z35 = x & 35 == 0

    return Za <= ((not Z31) <= (not Z35))


for a in reversed(range(50, 120 + 1)):
    if all(f(x, a) for x in range(1, 200)):
        print(a)
        exit()
