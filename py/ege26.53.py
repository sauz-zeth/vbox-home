from itertools import combinations
f = open('26-53.txt')
N = int(f.readline())
a = [int(f.readline()) for i in range(N)]

aodd = (x for x in a if x % 2 != 0)

avg = set(sum(c) // 2 for c in combinations(aodd, 2))

okavg = [x for x in a if x in avg]

print(len(okavg), max(okavg))
