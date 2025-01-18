from collections import deque

f = open('ege24.151.txt')
s = f.readline().strip()

w = deque(s[:5], maxlen = 5)
s = s[5:]

n = 0

for c in s:
    wa = list(w)
    if wa == wa[::-1]:
        n += 1
    w.append(c)

print(n)
