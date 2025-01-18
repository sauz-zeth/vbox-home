f = open("ege18.2.txt")
ga = (list(map(int, l.split())) for l in f if l != '\n')

npa = [0] * 10

for a in ga:
    na = []

    for i in range(10):
        x = a[i]
        ux = npa[i]
        lx = na[i - 1] if i >= 1 else 0

        na.append(max(ux, lx) + x)

    npa = na

print(na[9])

