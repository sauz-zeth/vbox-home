f = open('26-66.txt')
N, K = map(int, f.readline().split())
a = [tuple(map(int, f.readline().split())) for i in range(N)]
DAY = 24 * 60 * 60 * 1000
K1 = DAY + K


def parallel(t1, t2):
    x0, x1 = t1
    y0, y1 = t2

    if x1 < y0 or x0 > y1:
        return 0 
    return 1


pp = [[]]
for t1 in a:
    x0, x1 = t1

    if x0 == 0: x0 = K
    if x1 == 0: x1 = K1
    if x0 > x1: continue

    nt1 = (x0, x1)

    for p in pp:
        if all(parallel(nt1, nt2) for nt2 in p):
            p.append(nt1)
        else:
            pp.append([])
            pp[-1].append(nt1)

print(max(pp, key = len))
