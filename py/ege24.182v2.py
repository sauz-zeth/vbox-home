from collections import deque

f = open('24-181.txt')
s = f.readline().strip()

a = map(len, s.split('.'))

w = deque(maxlen = 3)

smax = 0

for x in a:
    w.append(x)

    s = sum(w)
    if s > smax:
        smax = s

print(smax + 2)
