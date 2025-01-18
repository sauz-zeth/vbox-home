from collections import deque

f = open('ege24.33.txt')
s = f.readline().strip()

def pairdiff(w):
    px = '.'
    for x in w:
        if x == px: return 0
        
        px = x

    return 1

ls = ['BCD', 'BDE', 'BCE']

n = 0
w = deque('..', maxlen = 3)

for x in s:
    w.append(x)
    if all(c in alpha for c, alpha in zip(w, ls)) and pairdiff(w):
        n += 1

print(n)
