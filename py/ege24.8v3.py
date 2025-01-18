f = open("ege24.8.txt")
s = f.read().strip()

n = 0
nmax = 0

for x in s:
    if x == 'C':
        n += 1

        if n > nmax:
            nmax = n
    else:
        n = 0

print(nmax)
