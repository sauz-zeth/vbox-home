f = open('26-89.txt')

N = int(f.readline())
a = sorted({int(f.readline()) for i in range(N)})

xmin = float('inf')
k = 0
while a:
    x = a.pop()

    if x <= xmin - 3:
        xmin = x
        k += 1

print(k, xmin)
