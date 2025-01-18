f = open("ege9.144.txt")

n = 0

for l in f:
    if l == '\n': continue

    ax = list(map(int, l.split()))

    if min(ax) < 1 or max(ax) > 8: continue

    ad = [ax[0] - ax[2], ax[1] - ax[3]]
    if sum(x ** 2 for x in ad) == 5:
        n += 1

print(n)
