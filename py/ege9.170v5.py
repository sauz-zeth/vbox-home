f = open("ege9.170.txt")
gax = (list(map(int, l.split())) for l in f if l != '\n')
gax_ = (ax for ax in gax if list(map(ax.count, ax)).count(1) == 4)

n = sum(5 * sum(x for x in ax if ax.count(x) == 1) <= 4 * sum(ax) for ax in gax_)
print(n)

