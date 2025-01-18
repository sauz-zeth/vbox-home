f = open('ege26.41.txt')
esmax, dsmax, n = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(n))

e = []
d = []

for x in a:
    if x > 500:
        e.append(x)
    else:
        d.append(x)

def maxsaved(maxsize, files):
    n = 0
    ps = 0
    s = 0
    for x in files:
        if s + x > maxsize:
            for y in reversed(files):
                if ps + y < maxsize:
                    return n, y

        n += 1
        ps = s
        s += x

print(*(dx + ex for dx, ex in zip(maxsaved(dsmax, d), maxsaved(esmax, e))))
