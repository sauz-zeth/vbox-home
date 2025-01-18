f = open('ege24.154.txt')
s = f.readline().strip()


n = 0
nmin = len(s)

for c in s:
    if n > 0:
        n += 1
        if c == 'D':
            if n > 2 and n < nmin: 
                nmin = n

            n = 1

    elif c == 'D':
        n = 1

print(nmin)
