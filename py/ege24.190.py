import re
from collections import deque

f = open('24-181.txt')

s = f.readline().strip()

#re.sub(r'[AEIOUY]', '#', s)

for x in 'AEIOUY':
    s = s.replace(x, '#')

a = [('#' in x, len(x)) for x in s.split('.')]

w1 = deque(maxlen=7)
w2 = deque(maxlen=7)

s = 0
smax = 0

for x, l in a:
    w1.append(x)
    if sum(w1) == 0:
        print('x')

    w2.append(l)

    if len(w1) < 7: continue

    if s > smax:
        smax = s

print(smax)
