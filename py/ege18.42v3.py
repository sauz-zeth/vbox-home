import itertools as it
from collections import deque

f = open("ege18.42.txt")

T = [list(map(int, l.split())) for l in f if l != '\n']
m = len(T[0])

def printT(A):
    for a in A:
        print(*("%4d" % x for x in a))
    print()

def step(A, strict = 1):
    iterA = it.chain([m * [0]], iter(A), [m * [0]])
    w = deque([next(iterA), next(iterA)], maxlen = 3)

    B = []

    for a in iterA:
        b = []
        
        w.append(a)
        upb, pb, dpb = w

        lpb = [0] + pb[:-1]
        rpb = pb[1:] + [0]
        
        for ux, x, dx, lx, rx in zip(upb, pb, dpb, lpb, rpb):
            delta = max(ux, dx, lx, rx) - x 
            isPeak = delta < 0 if strict else delta <= 0
            if isPeak and x > 0:
                b.append(min(0, ux, dx, lx, rx) - 1)
            else:
                b.append(x)

        B.append(b)

    return(B)

pB = []
B = [[x for x in a] for a in T]

while True:
    pB = B
    B = step(B)

    if pB != B:
        printT(B)
    else:
        pB = B
        B = step(B, strict = False)
        if pB == B: break
        printT(B)

print(-(min(x for a in B for x in a)))
