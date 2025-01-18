f = open("17-10.txt")
n = 0
s = 0
px = int(f.readline())
x = int(f.readline())

while True:
    l = f.readline()
    if l == '': break
    ppx = px
    px = x
    x = int(l)
    
    c = max(ppx, px, x)
    if ppx**2 + px**2 + x**2 == c**2 * 2:
        s += c
        n += 1

print (n, s)

