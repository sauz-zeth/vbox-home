f = open('ege24.159.txt')

s = f.readline().strip()

alpha = set(s)

a = []
b = []

for x in alpha:
    for y in alpha:
        w = x + y + x
        a.append((y, s.count(w)))


for c in alpha:
    b.append((c, sum(x[1] for x in a if x[0] == c)))

print(max(b, key = lambda a: a[1]))
