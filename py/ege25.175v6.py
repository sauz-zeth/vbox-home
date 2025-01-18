from math import isqrt

primes = []

def primeGen(x):
    primes.append(2)
    for i in range(3, x, 2):
        if factor(i) == i:
            primes.append(i)

def factor(x):
    if x < 2:
        return 0

    for j in primes:
        if j * j > x: break

        if x % j == 0:
            return j

    return x

def sieveGen(x):
    sieve = [1] * (x + 1)
    sieve[0] = sieve[1] = 0

    for i in primes:
        for j in range(i + i, x + 1, i):
            sieve[j] = 0

    return sieve


N = 3 * 10**6
M = 10 * 10**6

primeGen(isqrt(M))

sieve = sieveGen(M)

n = 0
for x in range(N + 7, M + 1, 6):
    if sieve[x] and sieve[x - 2]:
        n += 1
        r = x - 1 

print(n, r)
