from collections import Counter

f = open('ege24.164.txt')
g = (l.strip() for l in f if l != '\n')

nmaxmax = 0
for s in g:
    n = 1
    pc = ''
    nmax = 0
    for c in s:
        if c == pc:
            n += 1
        else:
            n = 1

        if n > nmax:
            nmax = n

        pc = c

    if nmax > nmaxmax:
        nmaxmax = nmax
        S = s

mc = Counter(S).most_common()
fmin = mc[-1][1]
cfmin = max(c for c, f in mc if f == fmin)

f.seek(0)
s = f.read()

cnt = Counter(s)

print(cfmin, cnt[cfmin], sep = '')
