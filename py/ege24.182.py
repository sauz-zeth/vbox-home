import re

f = open('24-181.txt')
s = f.readline().strip()

pat = re.compile(r'[^.]*[.]?[^.]*[.]?[^.]*')

lmax = 0

for i in range(len(s)):
    m = pat.match(s, i)
    if m is None: continue

    l = len(m[0])

    if l > lmax:
        lmax = l

print(lmax)
