def factor(x):
    if x < 2:
        return 0

    j = 2
    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x 

N = 158928
M = 345293
imin = M
n = 0

for i in range(N, M + 1):
    a = factor(i)
    if a == i: continue

    bc = i // a
    b = factor(bc)
    if b == bc: continue 
    if b == a: continue

    c = bc // b
    if c != factor(c): continue
    if c == b or c == a: continue

    n += 1

    if i < imin:
        imin = i

print(n, imin)
