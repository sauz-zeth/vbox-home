f = open("ege9.170.txt")
gax = (list(map(int, l.split())) for l in f if l != '\n')
gax_ = (ax for ax in gax if list(map(ax.count, ax)).count(1) == 4)

n = 0

for ax in gax_:
    snoreps = sum(x for x in ax if ax.count(x) == 1)
    sreps = sum(ax) - snoreps

    if snoreps <= sreps * 4:
        n += 1

print(n)

