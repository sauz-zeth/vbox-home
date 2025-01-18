from itertools import islice

f = open('26-k6.txt')
N, K = map(int, f.readline().split())
g = (dict(zip('wp', map(int, l.split()))) for l in islice(f, N))

a = sorted(g, key = lambda t: (t['p'] / t['w'], -t['w']))
b = sorted(a[:K], key = lambda t: t['w'])

print(sum(t['w'] for t in b), b[-1]['p'])
