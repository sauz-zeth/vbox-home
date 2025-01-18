f = open('26-55.txt')
N, S = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(N))

n = 0
k = 0

while k < N:
    w = 0

    for i in range(len(a) - 1, -1, -1):
        x = a[i]
        if x is None: continue
        if w + x <= S:
            w += x
            a[i] = None
            k += 1
    
    n += 1    

print(n, w)
