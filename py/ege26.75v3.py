f = open('26-75.txt')
N = int(f.readline())
a_ = (tuple(map(int, f.readline().split())) for i in range(N))
a_ = [(t0, -t1) for t0, t1 in a_]

a = []
for t0, t1 in a_:
    a.append(t0)
    a.append(t1)

a = sorted(a, key = abs)

c = 0
pc = 0
pt = 0

st = 0
cmax = 0

# ____[__[_]_]__[___

for t in a:
    if t >= 0:
        c += 1
    else:
        c -= 1
    
    if pc == 0:
        st += t + pt

    if c > cmax:
        cmax = c
    
    pt = t
    pc = c

print(cmax, abs(t) - st)
