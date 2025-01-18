f = open('ege26.62.txt')
N, M = map(int, f.readline().split())

ga = ((int(ps), t) for ps, t in map(str.split, f))
a = sorted(ga, key = lambda x: x[0])

s = M
n = 0

for x, _ in a:
    if s - x < 0: break
    s -= x
    n += 1

b = a[n - 1::-1]
c = a[n:]

def norm(): 
    global s
    l0 = 0
    for i in range(len(b)):
        if b[i][1] == 'Z':
            for l in range(l0, len(c)):
                if c[l][1] == 'Q':
                    ds = b[i][0] - c[l][0]
                    if s + ds < 0: return
                    s += ds
                    b[i] = c[l]
                    del c[l]
                    l0 = l
                    break

norm()

print(sum(1 for x in b if x[1] == 'Q'), s)

