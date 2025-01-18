import re

f = open('24-224.txt')
s = f.readline().strip()

pat = re.compile(r'(BAC|CAB)+')

nmax = 0
for i in range(len(s)):
    m = pat.match(s, i)
    if not m: continue

    n = len(m[0])

    if n > nmax:
        nmax = n

print(nmax)
