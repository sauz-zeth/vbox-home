from collections import deque

f = open('ege24.159.txt')

s = f.readline().strip()

alpha = set(s)

d = {}

w = deque(s[:2], maxlen = 3)

for c in s[2:]:
    w.append(c)

    if w[0] == w[2]:
        d[w[1]] = d.get(w[1], 0) + 1

cfmax = max(d, key = lambda x: d[x])
print(cfmax, d[cfmax], sep = '')
