def isEven(x):
    return x % 2 == 0

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

    if (isEven(pppx) and not isEven(ppx) and isEven(px) and not isEven(x) or
            not isEven(pppx) and isEven(ppx) and not isEven(px) and isEven(x)):
        n += 1
        s = pppx + ppx + px + x
        if s > smax:
            smax = s
print(n, smax)
