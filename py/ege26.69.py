#f = open('26-69.txt')
f = open('ege26.69-test.txt')
N = int(f.readline())
a = sorted(tuple(map(int, l.split())) for l in f if l != '\n')

nmax = 0
rmax = 0
pr, pc = a[0]

for r, c in a:
    if c - pc == 1 and r == pr:
        n += 1
    else:
        n = 1

    if n >= nmax:
        nmax = n
        rmax = r

    pr = r
    pc = c

print(rmax, nmax)
