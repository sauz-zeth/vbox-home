def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x


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

def dmaxFiltered(d, f):
    df = filter(f, d)

    return max(df, default = 0)

def A(x):
    d = divs(x)
    emax = dmaxFiltered(d, lambda x: x % 2 == 0)
    omax = dmaxFiltered(d, lambda x: x % 2 != 0)

    if emax and omax:
        return abs(emax - omax)
    else:
        return 0
    

N = 5
n = 0
i = 250156

while n < N:
    i += 1

    a = A(i)
        
    if factor(a) == a and a % 10 == 9:
        print(i, a)
        n += 1



