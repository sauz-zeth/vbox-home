import timer as tm

f = open('26-55.txt')
N, S = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(N))

tm.start()

n = 0
while a:
    w = 0

    for i in range(len(a) - 1, -1, -1):
        x = a[i]
        if w + x <= S:
            w += x
            a.pop(i)
    
    n += 1    

tm.show()

print(n, w)
