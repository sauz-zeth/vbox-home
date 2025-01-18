def ok(x1, x2):
    return (x1 + x2) % 2 != 0

f = open("17-3.txt")
n = 0
smax = 0
ppx = int(f.readline())
px = int(f.readline())
x = int(f.readline())

while True:
    l = f.readline()
    if l == '': break
    pppx = ppx
    ppx = px
    px = x
    x = int(l)

    if ok(pppx, ppx) and ok(ppx, px) and ok(px, x):
        n += 1
        s = pppx + ppx + px + x
        if s > smax:
            smax = s
print(n, smax)
