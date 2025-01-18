f = open("ege24.21.txt")
s = f.read().strip()

n = 0
nmax = 0
for c in s:
    if c in 'ABC':
        n += 1

        if n > nmax:
            nmax = n
    else:
        n = 0

print(nmax)
