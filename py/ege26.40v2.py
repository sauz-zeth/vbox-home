from bisect import bisect
from itertools import accumulate, islice

f = open('26-39.txt')
N, M = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(N))

i320 = bisect(a, 320) - 1
s1 = 0
n = 0
for i in range(i320, -1, -1):
    if a[i] < 310: break
    if s1 + a[i] > M: break
    s1 += a[i]
    n += 1

a[i + 1 : i320 + 1] = []

sa = list(accumulate(a, initial = s1))[1:]
imax = bisect(sa, M)
n += imax

a1 = a[:imax]
a2 = a[imax:]

j0 = len(a2) - 1
for i in range(len(a1) - 1, -1, -1):
    for j in range(j0, -1, -1):
        if sa[i - 1] + a2[j] + sum(islice(reversed(a1), len(a1) - i - 1)) <= M:
            a1[i] = a2[j]
            j0 = j - 1
            break

print(n, sum(a1) + s1)

