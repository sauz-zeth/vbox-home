def factor(x):
    if x < 2:
        return 0

    j = 2
    while j * j <= x:
        if x % j == 0:
            return j
        j += 1

    return x 

N = 158928
M = 345293
imin = M
n = 0

for i in range(N, M + 1):
    a = factor(i)
    bc = i // a
    b = factor(bc)

    if b > 0: 
        c = bc // b
    else:
        continue

    if a != b and b != c and a != c and factor(c) == c:
        n += 1
        if i < imin:
            imin = i

print(n, imin)
