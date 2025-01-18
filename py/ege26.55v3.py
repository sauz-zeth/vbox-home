import timer as tm

f = open('26-55.txt')
N, S = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(N))

n = 0

tm.start()

while a:
    w = 0

    for i in range(len(a) - 1, -1, -1):
        x = a[i]

        if w + x <= S:
            w += x
            if i == len(a) - 1:
                a.pop()
            else:
                a[i] = 0
    
    n += 1    

tm.show()

print(n, w)
