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

N = 3 * 10**6
M = 10 * 10**6

primeGen(10**4)

n = 0
for x in range(N + 7, M + 1, 6):
    if factor(x) == x and factor(x - 2) == x - 2:
        n += 1
        r = x - 1 

print(n, r)
