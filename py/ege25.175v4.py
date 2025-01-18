def sieveGen(x):
    sieve = [1] * x
    sieve[0] = sieve[1] = 0

    for i in range(int(x ** 0.5)):
        if sieve[i] == 0: continue
        for l in range(i + i, x, i):
            sieve[l] = 0

    return sieve


N = 3 * 10**6
M = 10 * 10**6

sieve = sieveGen(M)

n = 0
for x in range(N + 7, M + 1, 6):
    if sieve[x] and sieve[x - 2]:
        n += 1
        r = x - 1 

print(n, r)
