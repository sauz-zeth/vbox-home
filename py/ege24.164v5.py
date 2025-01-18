from collections import Counter

fs = open('ege24.164.txt').read()

def markup(s):
    pc = s[0]
    a = []
    for c in s:
        a.append(c)

        if c != pc:
            a.append('*')

        pc = c

    return ''.join(a)


nmax = lambda s: max(map(len, markup(s).split('*')))
S = max(fs.split(), key = nmax)

_, cfmin = max((-f, c) for c, f in Counter(S).items())

print(cfmin, Counter(fs)[cfmin], sep = '')
