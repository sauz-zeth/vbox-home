from collections import deque

f = open('ege24.156.txt')

s = f.readline().strip()

w = deque(s[:9], maxlen = 10)
n = 0

for c in s[9:]:
    w.append(c)

    if w[0] != 'A': continue

    n += list(w)[6:].count('F')
    
print(n)
