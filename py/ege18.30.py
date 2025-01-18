f = open("ege18.30.txt")

smax = 0
s = 0
x = float(f.readline())


while True:
    l = f.readline()
    if l == '': break
    px = x
    x = float(l)
    
    if x < px:
        s += x
    else:
        s = x

    if s > smax:
        smax = s

print(int(smax))
