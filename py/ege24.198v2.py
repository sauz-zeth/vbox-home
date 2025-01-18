f = open('ege24.198.txt')
s = f.read().strip()

nmax = 0
for i in range(len(s)):
    n = 0
    for j in range(i + 2, len(s), 3):
        if s[j - 2] in 'XZ' and s[j] == 'Y': 
            n += 1 
        else: break

    if n > nmax:
        nmax = n

print(nmax)
