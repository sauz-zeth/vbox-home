from bisect import bisect
from itertools import accumulate

def maxSumCount(a, m):
    sk = list(accumulate(a))
    n = bisect(sk, m)
    s = sk[n - 1]

    return s, n


f = open('26-39.txt')
N, M = map(int, f.readline().split())

a = []
b = []

for i in range(N):
    x = int(f.readline())
    if 310 <= x <= 320:
        b.insert(bisect(a, x), x)
    else:
        a.insert(bisect(a, x), x)

sb, nb = maxSumCount(reversed(b), M)
sa, na = maxSumCount(a, M - sb)
s = sa + sb
n = na + nb

a1 = a[:na]
a2 = a[na:]

while a1:
    x = a1.pop()
    while a2:
        y = a2.pop()
        if s - x + y <= M:
            s = s - x + y
            break

print(n, s)

