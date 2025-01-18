f = open('ege24.33.txt')
s = f.readline().strip()

ls = ['BCD', 'BDE', 'BCE']

n = 0
px = '.'
ppx = '.'

for x in s:
    if ppx in ls[0] and px in ls[1] and x in ls[2] and x != px and px != ppx:
        n += 1

    ppx = px
    px = x

print(n)
