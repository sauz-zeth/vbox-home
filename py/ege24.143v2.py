from collections import deque

f = open('ege24.143.txt')
g = (l.strip() for l in f if l != '\n')

n = 0
for l in g:
    w = deque(l[:3], maxlen = 4)

    for c in l[3:]:
        w.append(c)
        s = ''.join(w)
#        if s == f"Z{w[1]}RO":
        if s[0] + '*' + s[2:] == 'Z*RO':
            n += 1
            break

print(n)
