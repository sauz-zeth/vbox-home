f = open("ege9.170.txt")
gax = (list(map(int, l.split())) for l in f if l != '\n')

n = 0

for ax in gax:
    OneRep = False
    repCounts = []
    noreps = []

    for x in ax:
        repCounts.append(ax.count(x))

    if repCounts.count(1) != 4: continue

    for x in range(len(ax)):
        if repCounts[x] == 1: noreps.append(ax[x])

    Srep = sum(ax) - sum(noreps)

    if sum(noreps) <= Srep * 4:
        n += 1

print(n)

