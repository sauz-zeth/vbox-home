from collections import Counter

f = open('26-66.txt')
N, K = map(int, f.readline().split())
a = (tuple(map(int, f.readline().split())) for i in range(N))
DAY = 24 * 60 * 60 * 1000
K1 = DAY + K

a0 = Counter()
a1 = Counter()
for t0, t1 in a:
    a0[t0] += 1
    a1[t1 if t1 != 0 else K1] += 1

#_______[_|_|_|_]____

tnmax = 0
nmax = 0
n = 0
print(K1)
for t in range(0, K1 + 1):
    pn = n

    n += a0[t] - a1[t]

    if t % 1000000 == 0:
        print(nmax, tnmax, t, n)
    if t <= K: continue

    if n > nmax:
        nmax = n
        tnmax = 0

    if pn == nmax:
        tnmax += 1

print(nmax, tnmax)
