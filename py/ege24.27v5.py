f = open("ege24.27.txt")
s = f.read().strip()
alpha = 'EAB'

n = 0
nmax = 0

for c in s:
    x = alpha[n % 3]
    if c == x:
        n += 1

        if n > nmax:
            nmax = n
    elif c == 'E':
        n = 1
    else:
        n = 0

print(nmax)

