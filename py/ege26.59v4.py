from collections import namedtuple as nt
seat = nt('Seat', 'r c')

f = open('26-59.txt')
N = int(f.readline())
g = (seat._make(map(int, l.split())) for l in f if l != '\n')
a = sorted(g, key = lambda t: (-t.r, t.c))

pc = a[0].c
pr = a[0].r
for r, c in a:
    if c - pc == 3 and r == pr: break

    pr = r
    pc = c

print(r, pc + 1)
