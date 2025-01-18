from itertools import combinations

f = open('26-53.txt')
N = int(f.readline())
a = sorted(int(f.readline()) for i in range(N))

aodd = (x for x in a if x % 2 != 0)

avg = sorted(sum(c) // 2 for c in combinations(aodd, 2))

okavg = []
ax = a.pop()
y = avg.pop()

while avg and a:
    if y == ax:
        okavg.append(ax)
        ax = a.pop()
    elif y < ax:
        ax = a.pop()
        continue

    y = avg.pop()

print(len(okavg), max(okavg))
