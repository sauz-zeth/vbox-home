NMIN = 2 * 10**8 
IMAX = 5

def divs(x):
    j = 2
    d = []
    d1 = []

    while j * j < x:
        if x % j == 0:
            d.append(j)
            d1.append(x // j)

        j += 1

    if j * j == x:
        d.append(j)

    d += reversed(d1)

    return d

def D(o):
    return o[-6] if len(o) >= 6 else 0

n = NMIN
i = 0

while i < IMAX:
    n += 1

    o = list(filter(lambda x: x % 2 != 0, divs(n)))
    e = D(o)

    if e > 0:
        print(e, len(o))
        i += 1
