EMPTY = -1
f = open("17-3.txt")

n = 0
smax = 0
p = EMPTY
pp = EMPTY
x = int(f.readline())
px = 0
ppx = 0

while True:
    l = f.readline()
    if l == '': break
    pppx = ppx
    ppx = px
    px = x
    x = int(l)

    ppp = pp
    pp = p 
    p = (x + px) % 2 != 0 

    if p and pp and ppp and ppp != EMPTY:
        n += 1
        s = pppx + ppx + px + x
        if s > smax:
            smax = s

print(n, smax)
