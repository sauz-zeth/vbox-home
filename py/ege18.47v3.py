f = open("ege18.47.txt")

ax = [int(l) for l in f if l != '\n']

k = sum(ax[i] + ax[j] < 200 for i in range(11, len(ax)) for j in range(i - 11 + 1))

print(k)


