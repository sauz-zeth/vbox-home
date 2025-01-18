f = open("17-1.txt")

M = 10000
n = 0
x = int(f.readline())
smin = 2 * M
while True:
    l = f.readline()
    if l == '': break
    px = x
    x = int(l)

    s = x + px
    if (x % 7 == 0 and px % 17 != 0 or
        x % 17 != 0 and px % 7 == 0):
        if s < smin:
            smin = s
        n += 1
print (n, smin)

        n += 1
