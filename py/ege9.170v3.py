f = open("ege9.170.txt")
gax = (list(map(int, l.split())) for l in f if l != '\n')

n = 0

for ax in gax:
    noreps = [x for x in ax if ax.count(x) == 1]
    if len(noreps) != 4: continue

    snoreps = sum(noreps)
    sreps = sum(ax) - snoreps

    if snoreps <= sreps * 4:
        n += 1

print(n)

