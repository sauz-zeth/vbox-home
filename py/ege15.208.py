def nf(x, a):
    Za = x & a == 0
    Z62 = x & 62 == 0
    Z24 = x & 24 == 0

    f = ((not Za) <= (not Z62)) <= (Z24 and not Za)
    return not f

for a in range(1, 1000):
    if all(nf(x, a) for x in range(1, 1000)):
        print(a)
        break
