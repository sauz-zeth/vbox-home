fs = open('ege24.143.txt').read()
a = fs.split()

n = 0
for l in a:
    ppx, px, x = l[:3]

    for c in l[3:]:
        pppx = ppx
        ppx = px
        px = x
        x = c
        
#        if pppx + '*' + px + x == 'Z*RO':
        if pppx == 'Z' and px == 'R' and x == 'O':
            n += 1
            break

print(n)
