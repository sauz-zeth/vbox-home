f = open("ege9.170.txt")

n = 0

for l in f:
    if l == '\n': continue

    ax = list(map(int, l.split()))
    
    OneRep = False
    repCounts = []
    noreps = []
    reps = []

    for x in ax:
        repCounts.append(ax.count(x))

    if repCounts.count(1) == 4:
        OneRep = True

    for x in range(len(ax)):
        if repCounts[x] == 1: noreps.append(ax[x])

    for x in range(len(ax)):
        if repCounts[x] != 1: reps.append(ax[x])

    l = len(noreps)
    if l == 0: l = 1

    avgNoRep = sum(noreps) / l
    Srep = sum(reps)

    if avgNoRep <= Srep and OneRep:
        n += 1

print(n)

