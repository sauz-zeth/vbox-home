f = open("ege18.47.txt")

ax = [int(l) for l in f if l != '\n']

k = 0

for i in range(11, len(ax)):
    for j in range(i - 11 + 1):
        if ax[i] + ax[j] < 200:
            k += 1

print(k)


