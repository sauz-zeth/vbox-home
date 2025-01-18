from itertools import islice

f = open('26-k6.txt')
N, K = map(int, f.readline().split())
g1 = (tuple(map(int, l.split())) for l in islice(f, N))
g2 = ((p / w, -w, p) for w, p in g1)

a = sorted(g2)
b = sorted((-nw, p) for pw, nw, p in a[:K])

print(sum(t[0] for t in b), b[-1][1])
