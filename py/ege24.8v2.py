f = open("ege24.8.txt")
s = f.read().strip()

px = ''
n = 0
nmax = 0

for x in s:
    if x == 'C':
        if px == x:
            n += 1
        else:
            n = 1

        if n > nmax:
            nmax = n
    px = x

print(nmax)
