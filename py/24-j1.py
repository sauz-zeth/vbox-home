f = open('24-j1.utf8.txt')
g = open('24-j1.newline.txt', 'w')
s = f.readline().strip()

for c in s:
    print(c, file = g)

g.close()
