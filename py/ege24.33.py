f = open('ege24.33.txt')
s = f.readline().strip()

ls = [['B', 'C', 'D'], ['B', 'D', 'E'], ['B', 'C', 'E']]

size = 0
n = 0
px = ''

for x in s:
    k = 0
    for l in range(len(ls[0])):
        if x == ls[size % 3][l] and x != px:
            size += 1
            k = 1
            break
    if k == 0:
        if size == 3:
            n += 1
        size = 0

    px = x

print(n)
