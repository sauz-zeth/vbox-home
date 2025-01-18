f = open("17-339.txt")

n = 0
smax = 0
s = 0
xmin19 = 100000

while True:
    l = f.readline()
    if l == '': break
    x = int(l)
    if x > 0 and x % 19 == 0:
        if x < xmin19:
            xmin19 = x

f.seek(0)

x = int(f.readline())
while True:
    l = f.readline()
    if l == '': break
    px = x
    x = int(l)

    s = px + x
    if s < xmin19:
        n += 1
        if s > smax:
            smax = s

print (n, smax)

