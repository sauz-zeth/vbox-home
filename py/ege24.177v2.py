f = open('ege24.176.txt')

s = f.readline().strip()

pc = ''
n = 0
nmax = 0
for c in s:
    n += 1

    if c == 'P' and pc == 'R' or c == 'R' and pc == 'P':
        n = 1

    if n > nmax:
        nmax = n

    pc = c

print(nmax)
