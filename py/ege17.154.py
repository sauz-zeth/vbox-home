f = open("17-1.txt")

px = int(f.readline())
x = int(f.readline())
n = 0
nmin = 10000
k = 0
m = 0

while True:
    l = f.readline()
    if l == '': break
    ppx = px
    px = x
    x = int(l)

    n += 1

    if px > ppx and px > x:
        if n < nmin and k > 0:
            nmin = n
        n = 0
        k += 1

print(k, nmin)
