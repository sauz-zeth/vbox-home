import timer as tm

f = open('26-55.txt')
N, S = map(int, f.readline().split())
ga = (int(f.readline()) for i in range(N))
a = sorted(ga, reverse = 1)

tm.start()

n = 0
while a:
    w = 0

    b = []
    for x in a:
        if w + x <= S:
            w += x
        else:
            b.append(x)
    
    a = b
    n += 1   

tm.show()

print(n, w)
