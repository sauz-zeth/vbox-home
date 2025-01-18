from collections import deque

f = open('24-224.txt')
s = f.readline().strip()

an = [0, 0, 0]
w = deque(maxlen = 3)

nmax = 0
for i in range(len(s)):
    w.append(s[i])
    ws = ''.join(w)
    k = i % 3

    if ws == 'BAC' or ws == 'CAB':
        an[k] += 3
    else:
        an[k] = 0

    if an[k] > nmax:
        nmax = an[k]

print(nmax)
