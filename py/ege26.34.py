f = open('ege26.34.txt')

n = int(f.readline())
a = sorted(int(f.readline()) for i in range(n))

s = sum(a)

#s1 = s * 0.9
s1 = 489708.9

#s2 = s * 0.8
s2 = 435296.8

for i in range(n):
    dai = a[i] / 5
    s2 += dai
    ds = s1 - s2
    if ds < 0:
        l = ds + 2 * dai

        for j in range(i, n):
            daj = a[j] / 5
            if daj < l:
                ajmax = a[j]
        break

print(i, ajmax)
