f = open('ege24.77.txt')
s = f.read().strip()

px = ''
n = 0
nmax = 0

for x in s:
    if x != px:
        n += 1
    else:
        n = 1

    if n > nmax:
        nmax = n

    px = x

print(nmax)
