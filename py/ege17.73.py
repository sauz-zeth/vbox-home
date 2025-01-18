M = 1005
N = 147870
l = 0
l25 = 0
for i in range(N, M - 1, -1):
    x = i
    d1 = 0
    dmax = 0
    dmin = 9
    while x > 0:
        d = x % 10
        x //= 10
        if d == 1:
            d1 = 1
            break
        if d > dmax:
            dmax = d
        if d < dmin:
            dmin = d

    if dmax - dmin < 4 and not d1:
        l += 1
    if l == 25:
        l25 = i
print(l, l25)
