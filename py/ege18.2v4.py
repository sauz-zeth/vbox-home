import itertools as it
from math import inf

def sumMaxMin(m):
    E = 0 if m == max else inf

    f = open("ege18.2.txt")
    ga = (list(map(int, l.split())) for l in f if l != '\n')


    pb = it.chain([0], it.repeat(E))

    for a in ga:
        b = []

        ly = E
        for x, uy in zip(a, pb):
            y = m(uy, ly) + x
            b.append(y)

            ly = y 

        pb = b

    f.close()
    
    return b[-1]

print(sumMaxMin(max))
print(sumMaxMin(min))

