f = open("ege18.46.txt")
ax = [int(l) for l in f if l != '\n']

apx = []

for x in range(4):
    apx.append(-10000) 

apx.append(ax.pop(0))

n = 0

for x in ax:
    for px in apx:
        if 1500 > x + px > 1000:
            n += 1

    apx.pop(0)
    apx.append(x)

print(n)

