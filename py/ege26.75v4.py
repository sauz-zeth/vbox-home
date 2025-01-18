from collections import Counter

f = open('26-75.txt')

N = int(f.readline())
K = 10**6

a_ = (tuple(map(int, f.readline().split())) for i in range(N))

a0, a1 = map(Counter, zip(*a_))

# _|_[_|_]_|
c = 0
pc = 0
cmax = 0
st = 0
for t in range(K + 1):
    c += a0[t] - a1[t]

    if c > cmax:
        cmax = c

    if pc > 0:
        st += 1

    pc = c

print(cmax, st)
