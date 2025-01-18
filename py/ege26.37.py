from itertools import islice

f = open('26-k6.txt')
N, K = map(int, f.readline().split())
g = (tuple(map(int, l.split())) for l in islice(f, N))

a = sorted(g, key = lambda t: (t[1] / t[0], -t[0]))
b = sorted(a[:K])

print(sum(t[0] for t in b), b[-1][1])
