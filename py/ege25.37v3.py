def divCount(x):
    j = 2
    k = 2
    while j * j < x:
        if x % j == 0:
            k += 2
        j += 1 
    if j * j == x:
        k += 1
    
    return k

N = 248015
M = 251575
n = 0
k = 0

for l in range(399, 530, 2):
    i = l**2
    if i > M: break
    if N <= i <= M:
        k = divCount(i)
        n += 1
        print(n, i, k, l)
    


