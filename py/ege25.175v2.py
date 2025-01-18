def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x

N = 3 * 10**6
M = 10 * 10**6

n = 0

for x in range(N + 7, M + 1, 6):
    if factor(x) != x or factor(x - 2) != x - 2: continue

    n += 1
    r = x - 1 

print(n, r)
