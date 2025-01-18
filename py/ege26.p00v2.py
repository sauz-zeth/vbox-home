f = open('ege26.p00.txt')
s, n = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(n))

found = 0
for i, x in enumerate(a):
    s -= x
    if s < 0:
        if not found:
            found = 1
            print(i, end = ' ') 
            d = s + x 
            x1 = px + d

        if x1 < x:
            print(px)
            break

    px = x
        
