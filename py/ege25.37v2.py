def divCountSqrt(x):
    j = 2
    k = 2
    u = 0
    while j * j < x:
        if x % j == 0:
            k += 2
        j += 1 
    if j * j == x:
        k += 1
        u = j
    
    return k, u

N = 248015
M = 251575
n = 0
u = 0
k = 0

for i in range(N, M + 1, 2):
    k, u = divCountSqrt(i)
    if k % 2 == 0: continue
    n += 1
    print(n, i, k, u)

