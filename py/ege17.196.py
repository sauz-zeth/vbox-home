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

    if px**2 + x**2 == ppx**2:
        n += 1
        s += ppx

    elif x**2 + ppx**2 == px**2:
        n += 1
        s += px

    elif ppx**2 + px**2 == x**2:
        n += 1
        s += x

print (n, s)

