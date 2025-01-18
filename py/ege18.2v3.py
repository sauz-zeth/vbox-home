import itertools as it

f = open("ege18.2.txt")
ga = (list(map(int, l.split())) for l in f if l != '\n')


pb = it.repeat(0)

for a in ga:
    b = []

    ly = 0
    for x, uy in zip(a, pb):
        y = max(uy, ly) + x
        b.append(y)

        ly = y 

    pb = b

print(b[-1])

