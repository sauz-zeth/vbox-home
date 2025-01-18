def unique(t):
    return 100 <= t < 1000 and t % 2 != 0

f = open("17-199.txt")
n = 0
smax = 0
s = 0
px = int(f.readline())
x = int(f.readline())

while True:
    l = f.readline()
    if l == '': break
    ppx = px
    px = x
    x = int(l)

    if not unique(ppx) and unique(px) and not unique(x):
        n += 1
        s = ppx + px + x
        if s > smax:
            smax = s

print (n, smax)

