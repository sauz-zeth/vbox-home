from collections import deque

def tuplewise(a, l):
    w = deque(maxlen = l)

    for x in a:
        w.append(x)
        if len(w) == l:
            yield tuple(w) 

f = open('24-222.txt')
s = f.readline().strip()

a = s.split('A')[1:-1]

print(max(3 * len(x) for ppx, px, x in tuplewise(a, 3) if ppx == px == x) + 4)


