from itertools import chain

f = open('26-75.txt')
N = int(f.readline())
a_ = (tuple(map(int, f.readline().split())) for i in range(N))
a_ = [(t0, -t1) for t0, t1 in a_]

#a = chain(*zip(*a_))
#a = chain(*a_)
a0, a1 = zip(*a_)
a = a0 + a1
#a = (t for x in a_ for t in x)
a = sorted(a, key = abs)

c = 0
pc = 0
pt = 0

st = 0
cmax = 0

# ____[__[_]]_[_____

for t in a:
    if t >= 0:
        c += 1
    else:
        c -= 1

    if c > cmax:
        cmax = c
    
    if pc > 0:
        st += abs(t) - abs(pt)
    
    pt = t
    pc = c

print(cmax, st)
