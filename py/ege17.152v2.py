f = open("17-1.txt")

n = 0
x = int(f.readline())
xmax = -10000
while True:
    l = f.readline()
    if l == '': break
    px = x
    x = int(l)

    if (x % 9 == 0 and abs(px) % 8 == 3 and px % 9 != 0 or
        abs(x) % 8 == 3 and px % 9 == 0 and x % 9 != 0):
        n += 1
        m = max(px, x)
        xmax = max(xmax, m)
print (n, xmax)


