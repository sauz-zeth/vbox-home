D = 55 * 10**6
F = 60 * 10**6

def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x

for i in range(3, 100, 2):
    if factor(i) != i: continue

    x = i**4
    j = x

    while x <= F:
        if D <= x <= F:
            print(x, j)

        x *= 2
