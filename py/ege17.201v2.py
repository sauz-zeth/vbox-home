EMPTY = 10001
f = open("17-199.txt")
n = 0
smax = 0
s = 0
pu = 1
u = 1
px = EMPTY
x = EMPTY

while True:
    l = f.readline()
    if l == '': break
    ppx = px
    px = x
    x = int(l)
    
    ppu = pu
    pu = u
    u = 100 <= x < 1000 and x % 2 != 0

    if not ppu and pu and not u and ppx != EMPTY:
        n += 1
        s = ppx + px + x
        if s > smax:
            smax = s

print (n, smax)

