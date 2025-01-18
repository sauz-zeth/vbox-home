import re

f = open('ege24.198.txt')
s = f.read().strip()

pat = re.compile(r'(X.X|Y.Y)+')

nmax = 0
for i in range(len(s)):
    m = pat.match(s, i)
    if not m: continue

    n = len(m[0]) // 3

    if n > nmax:
        nmax = n

print(nmax)
