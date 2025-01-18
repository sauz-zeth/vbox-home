f = open('ege24.176.txt')

s = f.readline().strip()
alpha = set(s)


s = s.replace('QW', '<>')
for x in alpha:
    s = s.replace(x, '.')

w = ''

while w in s:
    w += '.'
    
print(len(w) - 1 + 2)
