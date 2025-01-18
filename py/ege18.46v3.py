f = open("ege18.46.txt")
gax = (int(l) for l in f if l != '\n')

apx = [None] * 5

n = 0

for x in gax:
    for px in apx:
        if px is not None and 1500 > x + px > 1000:
            n += 1

    apx.pop(0)
    apx.append(x)

print(n)

