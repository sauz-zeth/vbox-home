from itertools import permutations

alpha = 'ЭФЕКТ'

galpha = sorted('ЭЕ')
salpha = sorted('ФКТ', reverse = 1)

n = 0

for p in permutations(alpha, 5):
    g = [x for x in p if x in galpha]
    s = [x for x in p if x in salpha]

    if g == galpha and s == salpha:
        print(p)
        n += 1

print(n)

