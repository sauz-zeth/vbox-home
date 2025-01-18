f = open("18-k1.txt")

imax = 0
i = 0
while True:
    l = f.readline()
    if l == '': break
    x = int(l)

    if x % 2 != 0:
        i += 1
    else:
        i = 0

    if i > imax:
        imax = i

print(imax)
