f = open("ege9.144.txt")

g = (list(map(int, l.split())) for l in f if l != '\n')

n = 0
for ax in g:
    if all(1 <= x <= 8 for x in ax):
        x1, y1, x2, y2 = ax
        ad = [x1 - x2, y1 - y2]
        if sum(x ** 2 for x in ad) == 5:
            n += 1

print(n)
