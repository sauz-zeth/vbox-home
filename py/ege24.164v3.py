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

cfmin, fmin = max(Counter(S).items(), key = lambda x: (-x[1], x[0]))

f.seek(0)
cnt = Counter(f.read())

print(cfmin, cnt[cfmin], sep = '')
