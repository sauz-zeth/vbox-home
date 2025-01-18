f = open('ege24.154.txt')
s = f.readline().strip()


n = 0
nmin = len(s)
start = False

for c in s:
    if c == 'D':
        start = True

    if not start: continue

    if c != 'D':
        n += 1
    else:
        if n < nmin and n > 0:
            nmin = n
        n = 0

print(nmin + 2)
