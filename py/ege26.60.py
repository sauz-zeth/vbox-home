f = open('26-60.txt')
K, N = map(int, f.readline().split())
p = [int(f.readline()) for _ in range(K)]

a = [[] for _ in range(K)]
an = [0] * K

a0 = sorted((tuple(map(int, f.readline().split())) for _ in range(N)), reverse = True)

n = 0
for b, k in a0:
    an[k] += 1
    if len(a[k]) < p[k]:
        a[k].append(b)
        n += 1

krmax = max(range(K), key = lambda k: an[k] / p[k])

print(n, a[krmax][-1])
