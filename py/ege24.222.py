import re

f = open('24-222.txt')

s = f.readline().strip()

pat = re.compile(r'A([^A]+)(A\1){2}A')

lmax = 0

for i in range(len(s)):
    m = pat.match(s, i)
    if m is None: continue

    l = len(m[0])

    if l > lmax:
        lmax = l

print(lmax)
