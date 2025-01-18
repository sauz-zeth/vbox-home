import itertools as it
from collections import deque

f = open("ege18.42.txt")

b = [list(map(int, l.split())) for l in f if l != '\n']
m = len(b[0])
b.append(m * [0])

def printT(A):
    for a in A:
        for x in a:
            print("%4d " % x, end = "")
        print()
    print()

def depth(c, lvl):

    ppa = pa = m * [0]
    b = []
    v = deque([ppa, pa], maxlen = 3)

    for a in c:
        bx = []
        
        v.append(a)
        ppa, pa, a = v

        
        pxa = [0] + v[1]
        pxa.pop()

        nxa = v[1] + [0]
        nxa.pop(0)

        
        for u, x, d, px, nx in zip(ppa, pa, a, pxa, nxa):

            if lvl == 1:
                if max(u, d, px, nx) <= x:
                    bx.append(-1)
                else:
                    bx.append(x)

            else:
                if max(u, d, px, nx) < x and x > 0:
                    bx.append(min(u, d, px, nx) - 1)
                else:
                    bx.append(x)

        if bx != m * [0]:
            b.append(bx)

    b.append(m * [0])
    return(b)

lvl = 0
pb = []

while True:
    lvl += 1
    if pb == b: break

    pb = b
    b = depth(b, lvl)

    printT(b)

lastb = []

for i in range(len(b)):
  lastb.extend(b[i])

print(-(min(lastb)))
