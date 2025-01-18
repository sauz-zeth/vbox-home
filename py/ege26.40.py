f = open('26-39.txt')
N, M = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(N))

s1 = 0
k = 0
for x in range(320, 310 - 1, -1):
    while x in a:
        s1 += a.pop(a.index(x))
        k += 1

m = M - s1
n = 0

for x in a:
    if m - x < 0: break
    m -= x
    n += 1

m = M - s1
a1 = list(reversed(a[:n]))
a2 = list(reversed(a[n:]))

j0 = 0
for i in range(len(a1)):
    for j in range(j0, len(a2)):
        if sum(a1) - a1[i] + a2[j] <= m:
            a1[i] = a2[j]
            j0 = j + 1
            break

print(n + k, sum(a1) + s1)

