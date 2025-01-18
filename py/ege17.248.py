f = open("17-243.txt")
n = 0
s = 0
smin = 20000
xmax119 = 0

while True:
    l = f.readline()
    if l == '': break
    x = int(l)
    if x % 119 == 0:
        if x > xmax119:
            xmax119 = x

f.seek(0)
x = int(f.readline())

while True:
    l = f.readline()
    if l == '': break
    px = x
    x = int(l)

    if (px > xmax119 or x > xmax119) and (px % 100 == 21 or x % 100 == 21):
        s = x + px
        n += 1
        if s < smin:
            smin = s

print(n, smin)
