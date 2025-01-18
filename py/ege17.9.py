M = 1325
N = 15367
n = 0
imin = N
for i in range(M, N + 1):
    if i % 13 == 0 and i % 7 != 0 and \
       i % 17 != 0 and i % 19 != 0 and \
       i % 23 != 0:
            n += 1
            if i < imin:
                imin = i

print(n, imin)
