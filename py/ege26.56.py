from itertools import islice

f = open('ege26.56.txt')
V, K, N = map(int, f.readline().split())

files = sorted(map(int, islice(f, 0, N)), reverse = True)

disks = [V] * K
dbin = []

i = 0
k = 0

for x in files:
    k = 0
    while True:
        if disks[i % K] - x >= 0:
            disks[i % K] -= x
            i += 1
            break
        else:
            k += 1
            i += 1
            if k == K:
                dbin.append(x)
                break

print(sum(dbin), len(dbin))
            
