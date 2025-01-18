from collections import deque

def tuplewise(a, l = 2):
    w = deque(maxlen = l)
    for x in a:
        w.append(x)
        if len(w) == l:
            yield tuple(w)

f = open('24-181.txt')
s = f.readline().strip()

a = map(len, s.split('.'))

print(max(map(sum, tuplewise(a, 3))) + 2)
