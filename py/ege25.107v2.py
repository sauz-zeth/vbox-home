def isPrime(x):
    if x < 2:
        return False

    return factor(x) == x

def factor(x):
    if x < 2:
        return 0

    j = 2
    while j * j <= x:
        if x % j == 0:
            return j
        j += 1

    return x 

N = 153732
M = 225674
diffmin = M
idiffmin = 0
n = 0

for i in range(N, M + 1):
    a = factor(i)
    b = i // a

    if a != b and factor(b) == b:
        n += 1
        diff = abs(a - b)
        if diff < diffmin:
            diffmin = diff
            idiffmin = i

print(n, idiffmin)


    
