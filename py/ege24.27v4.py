from itertools import cycle

f = open("ege24.27.txt")
s = f.read().strip()
alpha = 'EAB'


w = ''
for x in cycle(alpha):
    w += x
    if w not in s: break
        
print(len(w) - 1)

