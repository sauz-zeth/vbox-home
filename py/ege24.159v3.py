from collections import deque, Counter

f = open('ege24.159.txt')

s = f.readline().strip()

alpha = set(s)

d = Counter()

w = deque(s[:2], maxlen = 3)

for c in s[2:]:
    w.append(c)

    if w[0] == w[2]:
        d[w[1]] += 1

print(*d.most_common(1)[0], sep = '')
