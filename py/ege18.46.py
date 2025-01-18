def ok(px):
    return 1500 > x + px > 1000 and px != E


f = open("18-k3.txt")
n = 0
E = -10000
px4 = E
px3 = E
px2 = E
px1 = E
x = E

while True:
    l = f.readline()
    if l == '': break
    px5 = px4
    px4 = px3
    px3 = px2
    px2 = px1
    px1 = x
    x = int(l)

    n += ok(px1) + ok(px2) + ok(px3) + ok(px4) + ok(px5)

print(n)

