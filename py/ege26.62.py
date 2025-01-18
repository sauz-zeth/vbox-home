f = open('ege26.62.txt')
N, M = f.readline().split()

lf = (x[:-1] for x in f) 

a = [tuple(x.split()) for x in lf]

za = sorted(int(x[0]) for x in a if x[1] == 'Z')
qa = sorted(int(x[0]) for x in a if x[1] == 'Q')

dm = int(M)
n = 0

for xz, xq in zip(za, qa):
    n += 1

    dm -= (xz + xq)
    if dm < 0:
        print(n, dm + xz)
        break
