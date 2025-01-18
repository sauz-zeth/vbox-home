f = open("ege24.52.txt")
s = f.read().strip()
alpha = set(s)

nmax = 0
n = 0
imin = len(s)
for c in alpha:
    w = ''

    while w in s:
        w += c

    w = w[:-1]
    n = len(w)
    i = s.index(w)
    
    if n > nmax:
        nmax = n
        imin = i
    elif n == nmax:
        if i < imin:
            imin = i


print(s[imin], nmax)

    
