f = open('26-66.txt')
N, K = map(int, f.readline().split())
DAY = 24 * 60 * 60 * 1000
K1 = DAY + K

g1 = (tuple(map(int, f.readline().split())) for i in range(N))
g2 = ((t0, -(t1 if t1 != 0 else K1)) for t0, t1 in g1)
a_ = [t for p in g2 for t in p]
a_ += [-K, K, -K1]
a = sorted(a_, key = abs)

#__[__]|[___[[_____[__[_______[___]|____]____

tnmax = 0
nmax = 0
n = 0
pt = 0
for t_ in a:
    t = abs(t_)

    if t > K1: break

    if n > nmax and t > K:
        nmax = n
        tnmax = 0

    if n == nmax and t > K:
        tnmax += t - pt

    pt = t
    n += 1 if t_ >= 0 else -1

print(nmax, tnmax)
