f = open("ege18.47.txt")

e = [int(l) for l in f if l != '\n']

k = 0
apx = [] 
n = 0

for x in e:

    if n < 11:
        n += 1
        continue

    apx.append(e[n - 11])

    for px in apx:
        if px + x < 200:
            k += 1

    n += 1

print(k)


