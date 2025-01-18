f = open('ege24.154.txt')
s = f.readline().strip()

for x in 'ABCEF':
    s = s.replace(x, '.')

w = '.'

while 'D' + w + 'D' not in s:
    w += '.'

n = len('D' + w + 'D')

print(n)
