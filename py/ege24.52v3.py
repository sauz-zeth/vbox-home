f = open("ege24.52.txt")
s = f.read().strip()
    
n = 1
nmax = 1
cn = ''

for c in s:
    if c == cn:
        n += 1
    else:
        cn = c
        n = 1

    if n > nmax:
        nmax = n
        cnmax = cn

print(cnmax, nmax)
