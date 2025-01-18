f = open("ege24.52.txt")
s = f.read().strip()
    
n = 1
nmax = 1
pc = ''

for c in s:
    if c == pc:
        n += 1
        cn = c
    else:
        n = 1

    if n > nmax:
        nmax = n
        cnmax = cn

    pc = c

print(cnmax, nmax)
