def sieveGen(x):
    sieve = [1] * (x + 1)
    sieve[0] = sieve[1] = 0
    
    i = 2
    while i * i <= x:
        if sieve[i] == 1:
            for j in range(i + i, x + 1, i):
                sieve[j] = 0

        i += 2 if i > 2 else 1

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
