D = 113 * 10**6
F = 114 * 10**6

def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x

for i in range(7500, 7600):
    if factor(i) != i: continue

    x = i**2 * 2

    if x < D: continue
    if x > F: break

    print(x, i)
