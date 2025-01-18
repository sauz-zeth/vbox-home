def isPrime(x):
    if x < 2:
        return False
    
    j = 2
    while j * j <= x:
        if x % j == 0:
            return False
        j += 2 if j > 2 else 1

    return True

n = 0
N = 200000
for i in range(2, N + 1):
    if isPrime(i):
        n += 1

print(n)
