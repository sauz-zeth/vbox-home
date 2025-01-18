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

    if (100 <= px < 1000 and px % 2 != 0
      and (x < 100 or x >= 1000 or x % 2 == 0)
      and (ppx < 100 or ppx >= 1000 or ppx % 2 == 0)):
        n += 1
        s = ppx + px + x
        if s > smax:
            smax = s

print (n, smax)

