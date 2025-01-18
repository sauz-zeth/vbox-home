N = 10000
M = 10000
n = 0
px = int(input())
smin = 2 * M
for i in range(N - 1):
    x = int(input())
    s = x + px
    if (x % 7 == 0 and px % 17 != 0 or
        x % 17 != 0 and px % 7 == 0):
        if s < smin:
            smin = s
        n += 1
    px = x
print (n, smin)

