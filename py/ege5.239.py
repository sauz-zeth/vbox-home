def dec2base(x, b):
    s = ''
    while x > 0:
        s = str(x % b) + s
        x = x // b

    return s

def f(i):
    si6 = dec2base(i, 6)
    si6 += si6[-1]

    si2 = bin(int(si6, 6))
    si2 += si2[-1]

    return int(si2, 2)

rmax = 0

for i in range(1, 1000):
    r = f(i)

    if rmax < r < 344:
        rmax = r
          

print(rmax)

