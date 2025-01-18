f = open("ege18.2.txt")

npa = [0] * 10

while True:
    l = f.readline()
    if l == '': break
    a = list(map(int, l.split()))
    na = []

    for i in range(10):
        x = a[i]
        ux = npa[i]
        lx = na[i - 1] if i >= 1 else 0

        na.append(max(ux, lx) + x)

    npa = na

print(na[9])

