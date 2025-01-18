NMAX = 300000000
IMAX = 5
UDN = -5
UNIQUE = 17

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

def unique(x):
    s = 0
    j = 0
    while x > 0:
        j = x % 10
        s += j
        x //= 10

    return s == UNIQUE

def filt(d):
    ud = []
    for i in d:
        if unique(i):
            ud.append(i)

    return ud

def D(ud):
    return 0 if len(ud) < 5 else ud[UDN]


n = NMAX
i = 0

ae = []
auk = []

while i < IMAX:
    n -= 1
    ud = filt(divs(n))

    e = D(ud)

    if e > 0:
        ae.append(e)
        auk.append(len(ud))
        i += 1

for i in range(IMAX - 1, -1, -1):
    print(ae[i], auk[i])
