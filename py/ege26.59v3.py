f = open('26-59.txt')
N = int(f.readline())
a = [tuple(map(int, t.split())) for t in f]
rows = sorted(set(x[0] for x in a))

hall = {r: set() for r in rows}

for r, c in a:
    hall[r].add(c)

for r in reversed(rows):
    cols = sorted(hall[r])
    pc = cols[0]
    for c in cols:
        if c - pc == 3:
            print(r, pc + 1)
            exit()

        pc = c
