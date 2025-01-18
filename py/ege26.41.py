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
    s = [0] 
    for x in files:
        if s[-1] + x > maxsize:
            for y in reversed(files):
                if s[-2] + y < maxsize:
                    return [len(s) - 1, y]

        s.append(s[-1] + x)

print(*(x + y for x, y in zip(maxsaved(dsmax, d), maxsaved(esmax, e))))
