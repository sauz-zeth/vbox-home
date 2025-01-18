f = open('ege24.197.txt')
s = f.read().strip()

s = s.replace('ZXY', '.')
s = s.replace('ZYX', '.')

w = ''

while w in s:
    w += '.'

print(len(w) - 1)

