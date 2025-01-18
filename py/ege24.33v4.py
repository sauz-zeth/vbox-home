from collections import deque

f = open('ege24.33.txt')
s = f.readline().strip()

def tuplewise(w, n = 2):
    d = deque([], maxlen = n)
    for x in w:
        d.append(x)
        if len(d) < n: continue
        
        yield tuple(d)

ls = ['BCD', 'BDE', 'BCE']

n = 0
w = deque('..', maxlen = 3)

for x in s:
    w.append(x)
    if all(c in alpha for c, alpha in zip(w, ls)) and all(x != y for x, y in tuplewise(w)):
        n += 1

print(n)
