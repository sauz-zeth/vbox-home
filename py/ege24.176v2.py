f = open('ege24.176.txt')

s = f.readline().strip()

nmax = 0
n = 0
px = ''

for x in s:
    n += 1

    if px == 'Q' and x == 'W':
        n = 1

    if n > nmax:
        nmax = n
        
    px = x

print(nmax)
