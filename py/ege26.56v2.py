from itertools import islice

f = open('ege26.56.txt')
V, K, N = map(int, f.readline().split())

files = sorted(map(int, islice(f, 0, N)), reverse = True)

disks = [V] * K
dbin = []

i = 0

for x in files:
    pos = -1
    while True:
        if disks[i % K] - x >= 0:
            disks[i % K] -= x
            i += 1
            break

        elif pos != -1:
            if i % K == pos:
                dbin.append(x)
                break

        else:
            pos = i % K

        i += 1

print(sum(dbin), len(dbin))
            
