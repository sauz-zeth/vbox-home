from collections import Counter

f = open('ege24.164.txt')
g = (l.strip() for l in f if l != '\n')

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
S = max(g, key = nmax)

nfmin, cfmin = max((-f, c) for c, f in Counter(S).items())

f.seek(0)
cnt = Counter(f.read())

print(cfmin, cnt[cfmin], sep = '')
