def divSumProper(x):
    s = 1
    j = 2
    while j * j < x:
        if x % j == 0:
            s += j + x // j
        j += 1
    if j * j == x:
        s += j

    return s


N = 30000
for i in range(2, N + 1):
    s = divSumProper(i)
    if s > i and divSumProper(s) == i:
        print(i, s)
