f = open('26-59.txt')
N = int(f.readline())
a = [tuple(map(int, t.split())) for t in f]
n = sorted(set(x[0] for x in a))
m = sorted(set(x[1] for x in a))

hall = {x: {y: 0 for y in range(m[0], m[-1] + 1)} for x in n}

for x, y in a:
    hall[x][y] = 1

for x in reversed(n):
    s = ''.join(map(str, hall[x].values()))
    if '1001' in s:
        print(x, s.index('1001') + min(m) + 1)
        break
