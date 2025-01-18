f = open("ege9.99.txt")

smax = 0

for l in f:
    if l == '\n': continue
    ax = list(map(int, l.split())) 
    
    m = max(ax)
    if sum(x * x for x in ax) == 2 * m**2:
        s = sum(ax) - m
        if s > smax:
            smax = s

print(smax)
