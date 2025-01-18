f = open('ege24.196.txt')
s = f.read().strip()

s = s.replace('ZX', '.')
s = s.replace('ZY', '.')

w = ''

while w in s:
    w += '.'

print(len(w) - 1)

