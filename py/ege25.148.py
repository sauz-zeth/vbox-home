D = 113 * 10**6
F = 114 * 10**6

def divs(x):
    j = 1
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

for i in range(D, F + 1):
    d = divs(i)

    de = [x for x in d if x % 2 == 0]

    if len(de) == 3:
        print(i, d[-3])
