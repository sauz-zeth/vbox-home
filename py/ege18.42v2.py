import itertools as it
from collections import deque

f = open("ege18.42.txt")

T = [list(map(int, l.split())) for l in f if l != '\n']
m = len(T[0])

def printT(A):
    for a in A:
        print(*("%4d" % x for x in a))
    print()

def depth(A):
    upb = pb = m * [0]
    B = []
    w = deque([upb, pb], maxlen = 3)

    for a in A:
        b = []
        
        w.append(a)
        upb, pb, dpb = w

        lpb = [0] + pb[:-1]
        rpb = pb[1:] + [0]
        
        for ux, x, dx, lx, rx in zip(upb, pb, dpb, lpb, rpb):
            if max(ux, dx, lx, rx) < x and x > 0:
                b.append(min(0, ux, dx, lx, rx) - 1)
            else:
                b.append(x)

        if b != m * [0]:
            B.append(b)

    B.append(m * [0])
    return(B)

pB = []

B = [[x for x in a] for a in T]
B += [m * [0]]

while True:
    if pB == B: break

    pB = B
    B = depth(B)

    printT(B)

lastB = (x for a in B for x in a)

print(-(min(lastB)))
