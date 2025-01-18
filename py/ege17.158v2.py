f = open("17-1.txt")

k = 0
n = 0
x = -10000
nmax = 0
while True:
    l = f.readline()
    if l == '': break
    px = x
    x = int(l)

    if x < px:
        n += 1
    else:
        n = 1

    if n > nmax:
        nmax = n
        k = 1
    elif n == nmax:
        k += 1

print(nmax, k)
